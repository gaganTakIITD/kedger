#pragma once

#include "engine.h"
#include "types.h"

#include <fstream>
#include <sstream>
#include <string>
#include <vector>

#include <nlohmann/json.hpp>

namespace returns {
namespace io {

inline std::vector<CategoryRule> loadCategoryRules(const std::string& path) {
    std::ifstream in(path);
    if (!in) {
        throw std::runtime_error("Failed to open category rules: " + path);
    }

    nlohmann::json data;
    in >> data;

    std::vector<CategoryRule> rules;
    for (const auto& item : data) {
        CategoryRule rule;
        rule.category = item.at("category").get<std::string>();
        rule.returnable = item.at("returnable").get<bool>();
        rule.allowed_return_window_days = item.at("allowed_return_window_days").get<int>();
        rules.push_back(rule);
    }
    return rules;
}

inline std::vector<ScoringRule> loadScoringRules(const std::string& path) {
    std::ifstream in(path);
    if (!in) {
        throw std::runtime_error("Failed to open scoring rules: " + path);
    }

    nlohmann::json data;
    in >> data;

    std::vector<ScoringRule> rules;
    for (const auto& item : data) {
        ScoringRule rule;
        rule.attribute = item.at("rule").get<std::string>();
        for (const auto& range : item.at("ranges")) {
            ScoreRange score_range;
            score_range.min = range.at("min").get<int>();
            score_range.max = range.at("max").get<int>();
            score_range.points = range.at("points").get<int>();
            rule.ranges.push_back(score_range);
        }
        rules.push_back(rule);
    }
    return rules;
}

inline std::vector<AccountProfile> loadAccountProfiles(const std::string& path) {
    std::ifstream in(path);
    if (!in) {
        throw std::runtime_error("Failed to open account profiles: " + path);
    }

    std::vector<AccountProfile> profiles;
    std::string line;
    while (std::getline(in, line)) {
        if (line.empty()) {
            continue;
        }
        auto item = nlohmann::json::parse(line);
        AccountProfile profile;
        profile.account_id = item.at("account_id").get<std::string>();
        profile.return_history_count = item.at("return_history_count").get<int>();
        profiles.push_back(profile);
    }
    return profiles;
}

inline std::vector<AccountLink> loadAccountLinks(const std::string& path) {
    std::ifstream in(path);
    if (!in) {
        throw std::runtime_error("Failed to open account links: " + path);
    }

    std::vector<AccountLink> links;
    std::string line;
    while (std::getline(in, line)) {
        if (line.empty()) {
            continue;
        }
        auto item = nlohmann::json::parse(line);
        AccountLink link;
        link.primary_account_id = item.at("primary_account_id").get<std::string>();
        link.related_account_id = item.at("related_account_id").get<std::string>();
        link.link_type = item.at("link_type").get<std::string>();
        links.push_back(link);
    }
    return links;
}

inline std::vector<ReturnRequest> loadReturnRequests(const std::string& path) {
    std::ifstream in(path);
    if (!in) {
        throw std::runtime_error("Failed to open return requests: " + path);
    }

    std::vector<ReturnRequest> requests;
    std::string line;
    while (std::getline(in, line)) {
        if (line.empty()) {
            continue;
        }
        auto item = nlohmann::json::parse(line);
        ReturnRequest request;
        request.request_id = item.at("request_id").get<std::string>();
        request.account_id = item.at("account_id").get<std::string>();
        request.category = item.at("category").get<std::string>();
        request.days_since_purchase = item.at("days_since_purchase").get<int>();
        request.order_value_usd = item.at("order_value_usd").get<int>();
        request.account_age_days = item.at("account_age_days").get<int>();
        request.total_return_history = 0;
        requests.push_back(request);
    }
    return requests;
}

inline void writeResults(const std::string& path, const std::vector<ReturnResult>& results) {
    std::ofstream out(path);
    if (!out) {
        throw std::runtime_error("Failed to open results file: " + path);
    }

    for (const auto& result : results) {
        nlohmann::json item;
        item["request_id"] = result.request_id;
        if (result.risk_score.has_value()) {
            item["risk_score"] = *result.risk_score;
        } else {
            item["risk_score"] = nullptr;
        }
        item["decision"] = result.decision;
        if (result.reason.has_value()) {
            item["reason"] = *result.reason;
        }
        out << item.dump() << '\n';
    }
}

}  // namespace io
}  // namespace returns
