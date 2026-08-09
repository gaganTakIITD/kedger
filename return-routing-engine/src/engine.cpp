#include "engine.h"

#include <algorithm>

namespace returns {

void Engine::build(const std::vector<CategoryRule>& category_rules,
                   const std::vector<ScoringRule>& scoring_rules,
                   const std::vector<AccountProfile>& profiles,
                   const std::vector<AccountLink>& links) {
    category_rules_.clear();
    for (const auto& rule : category_rules) {
        category_rules_[rule.category] = rule;
    }

    scoring_rules_ = scoring_rules;

    profile_map_.clear();
    for (const auto& profile : profiles) {
        profile_map_[profile.account_id] = profile.return_history_count;
    }

    account_groups_.clear();
    for (const auto& link : links) {
        // Store links bidirectionally so both accounts see each other.
        account_groups_[link.primary_account_id].insert(link.related_account_id);
        account_groups_[link.related_account_id].insert(link.primary_account_id);
    }

    // Transitively close each group so all members see all others.
    bool changed = true;
    while (changed) {
        changed = false;
        for (auto& [id, group] : account_groups_) {
            std::unordered_set<std::string> expanded = group;
            for (const auto& member : group) {
                auto it = account_groups_.find(member);
                if (it != account_groups_.end()) {
                    for (const auto& transitive : it->second) {
                        if (transitive != id && expanded.find(transitive) == expanded.end()) {
                            expanded.insert(transitive);
                            changed = true;
                        }
                    }
                }
            }
            group = expanded;
        }
    }
}

int Engine::totalReturnHistory(const std::string& account_id) const {
    int total = 0;

    auto profile_it = profile_map_.find(account_id);
    if (profile_it != profile_map_.end()) {
        total += profile_it->second;
    }

    auto group_it = account_groups_.find(account_id);
    if (group_it != account_groups_.end()) {
        for (const auto& linked_id : group_it->second) {
            auto linked_profile = profile_map_.find(linked_id);
            if (linked_profile != profile_map_.end()) {
                total += linked_profile->second;
            }
        }
    }

    return total;
}

int Engine::calculateRiskScore(const ReturnRequest& request) const {
    int total_points = 0;

    for (const auto& rule : scoring_rules_) {
        int value = 0;
        if (rule.attribute == "account_age_days") {
            value = request.account_age_days;
        } else if (rule.attribute == "order_value_usd") {
            value = request.order_value_usd;
        } else if (rule.attribute == "days_since_purchase") {
            value = request.days_since_purchase;
        } else if (rule.attribute == "total_return_history") {
            value = request.total_return_history;
        } else {
            continue;
        }

        for (const auto& range : rule.ranges) {
            if (value >= range.min && value <= range.max) {
                total_points += range.points;
                break;
            }
        }
    }

    return std::clamp(total_points, 0, 100);
}

std::string Engine::decisionForScore(int score) const {
    if (score <= 49) {
        return "AUTO_APPROVE";
    }
    if (score <= 74) {
        return "MANUAL_REVIEW";
    }
    return "REJECT";
}

std::optional<std::string> Engine::reasonForDecision(const std::string& decision) const {
    if (decision == "MANUAL_REVIEW") {
        return "MEDIUM_RISK_SCORE";
    }
    if (decision == "REJECT") {
        return "HIGH_RISK_SCORE";
    }
    return std::nullopt;
}

ReturnResult Engine::process(const ReturnRequest& request) const {
    ReturnResult result;
    result.request_id = request.request_id;

    auto category_it = category_rules_.find(request.category);
    if (category_it == category_rules_.end() || !category_it->second.returnable) {
        result.risk_score = std::nullopt;
        result.decision = "REJECT";
        result.reason = "CATEGORY_NON_RETURNABLE";
        return result;
    }

    if (request.days_since_purchase > category_it->second.allowed_return_window_days) {
        result.risk_score = std::nullopt;
        result.decision = "REJECT";
        result.reason = "RETURN_WINDOW_EXPIRED";
        return result;
    }

    ReturnRequest scored_request = request;
    scored_request.total_return_history = totalReturnHistory(request.account_id);

    const int risk_score = calculateRiskScore(scored_request);
    const std::string decision = decisionForScore(risk_score);

    result.risk_score = risk_score;
    result.decision = decision;
    result.reason = reasonForDecision(decision);

    return result;
}

}  // namespace returns
