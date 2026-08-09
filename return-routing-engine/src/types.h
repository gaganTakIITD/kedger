#pragma once

#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <optional>

namespace returns {

struct CategoryRule {
    std::string category;
    bool returnable;
    int allowed_return_window_days;
};

struct ScoreRange {
    int min;
    int max;
    int points;
};

struct ScoringRule {
    std::string attribute;
    std::vector<ScoreRange> ranges;
};

struct AccountProfile {
    std::string account_id;
    int return_history_count;
};

struct AccountLink {
    std::string primary_account_id;
    std::string related_account_id;
    std::string link_type;
};

struct ReturnRequest {
    std::string request_id;
    std::string account_id;
    std::string category;
    int days_since_purchase;
    int order_value_usd;
    int account_age_days;
    int total_return_history;  // computed at scoring time
};

struct ReturnResult {
    std::string request_id;
    std::optional<int> risk_score;
    std::string decision;
    std::optional<std::string> reason;
};

}  // namespace returns
