#pragma once

#include "types.h"

#include <string>
#include <vector>

namespace returns {

class Engine {
public:
    void build(const std::vector<CategoryRule>& category_rules,
               const std::vector<ScoringRule>& scoring_rules,
               const std::vector<AccountProfile>& profiles,
               const std::vector<AccountLink>& links);

    ReturnResult process(const ReturnRequest& request) const;

private:
    std::unordered_map<std::string, CategoryRule> category_rules_;
    std::vector<ScoringRule> scoring_rules_;
    std::unordered_map<std::string, int> profile_map_;
    std::unordered_map<std::string, std::unordered_set<std::string>> account_groups_;

    int totalReturnHistory(const std::string& account_id) const;
    int calculateRiskScore(const ReturnRequest& request) const;
    std::string decisionForScore(int score) const;
    std::optional<std::string> reasonForDecision(const std::string& decision) const;
};

}  // namespace returns
