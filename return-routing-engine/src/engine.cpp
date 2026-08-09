#include "engine.hpp"

#include <algorithm>
#include <cmath>

namespace returns {

Engine Engine::build(
    const std::vector<CategoryRule>& categories,
    const std::vector<ScoringRule>& scoring_rules,
    const std::vector<DecisionBand>& decision_bands,
    const std::unordered_map<std::string, int>& account_profiles,
    const std::vector<AccountLink>& links) {
  Engine engine;
  engine.scoring_rules_ = scoring_rules;
  engine.decision_bands_ = decision_bands;
  engine.account_profiles_ = account_profiles;

  for (const auto& cat : categories) {
    engine.categories_[cat.category] = cat;
  }

  // Build undirected adjacency. THIS IS THE ONE-WAY LINK BUG FIX:
  // store both primary -> related AND related -> primary.
  std::unordered_map<std::string, std::unordered_set<std::string>> account_groups;
  for (const auto& link : links) {
    account_groups[link.primary_account_id].insert(link.related_account_id);
    account_groups[link.related_account_id].insert(link.primary_account_id);
  }

  // Transitively close each group so all members see all others.
  bool changed = true;
  while (changed) {
    changed = false;
    for (auto& [id, group] : account_groups) {
      std::unordered_set<std::string> expanded = group;
      for (const auto& member : group) {
        auto it = account_groups.find(member);
        if (it == account_groups.end()) {
          continue;
        }
        for (const auto& transitive : it->second) {
          if (transitive != id && expanded.find(transitive) == expanded.end()) {
            expanded.insert(transitive);
            changed = true;
          }
        }
      }
      group.swap(expanded);
    }
  }

  // Ensure every account includes itself in its lookup group.
  for (auto& [id, group] : account_groups) {
    group.insert(id);
  }

  engine.account_groups_ = std::move(account_groups);
  return engine;
}

int Engine::linked_return_history(const std::string& account_id) const {
  int total = 0;
  auto group_it = account_groups_.find(account_id);
  if (group_it == account_groups_.end()) {
    auto profile_it = account_profiles_.find(account_id);
    return profile_it == account_profiles_.end() ? 0 : profile_it->second;
  }

  for (const auto& member : group_it->second) {
    auto profile_it = account_profiles_.find(member);
    if (profile_it != account_profiles_.end()) {
      total += profile_it->second;
    }
    // missing profile => 0
  }
  return total;
}

int Engine::score_request(const ReturnRequest& request,
                          int return_history_count) const {
  int score = 0;
  for (const auto& rule : scoring_rules_) {
    double value = 0.0;
    if (rule.attribute == "account_age_days") {
      value = static_cast<double>(request.account_age_days);
    } else if (rule.attribute == "return_history_count") {
      value = static_cast<double>(return_history_count);
    } else if (rule.attribute == "order_value_usd") {
      value = request.order_value_usd;
    } else {
      continue;
    }

    for (const auto& range : rule.ranges) {
      if (value >= range.min && value <= range.max) {
        score += range.points;
        break;
      }
    }
  }

  return std::clamp(score, 0, 100);
}

const DecisionBand* Engine::band_for(int score) const {
  for (const auto& band : decision_bands_) {
    if (score >= band.min && score <= band.max) {
      return &band;
    }
  }
  return nullptr;
}

RoutingResult Engine::route(const ReturnRequest& request) const {
  RoutingResult result;
  result.request_id = request.request_id;

  // Step 1a: category eligibility
  auto cat_it = categories_.find(request.category);
  if (cat_it == categories_.end() || !cat_it->second.returnable) {
    result.risk_score = -1;
    result.decision = "REJECT";
    result.reason = "CATEGORY_NON_RETURNABLE";
    return result;
  }

  // Step 1b: return window
  if (request.days_since_purchase > cat_it->second.allowed_return_window_days) {
    result.risk_score = -1;
    result.decision = "REJECT";
    result.reason = "RETURN_WINDOW_EXPIRED";
    return result;
  }

  // Step 2: risk score (linked history + scoring rules)
  const int history = linked_return_history(request.account_id);
  const int score = score_request(request, history);
  result.risk_score = score;

  // Step 3: decision + reason
  const DecisionBand* band = band_for(score);
  if (band == nullptr) {
    result.decision = "REJECT";
    result.reason = "HIGH_RISK_SCORE";
    return result;
  }

  result.decision = band->decision;
  result.reason = band->reason;  // empty for AUTO_APPROVE
  return result;
}

nlohmann::json Engine::to_json(const RoutingResult& result) const {
  nlohmann::json out;
  out["request_id"] = result.request_id;
  if (result.risk_score < 0) {
    out["risk_score"] = nullptr;
  } else {
    out["risk_score"] = result.risk_score;
  }
  out["decision"] = result.decision;
  if (!result.reason.empty()) {
    out["reason"] = result.reason;
  }
  return out;
}

}  // namespace returns
