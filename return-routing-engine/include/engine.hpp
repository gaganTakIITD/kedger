#pragma once

#include <nlohmann/json.hpp>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

namespace returns {

struct AccountLink {
  std::string primary_account_id;
  std::string related_account_id;
  std::string link_type;
};

struct CategoryRule {
  std::string category;
  bool returnable = false;
  int allowed_return_window_days = 0;
};

struct ScoreRange {
  int min = 0;
  int max = 0;
  int points = 0;
};

struct ScoringRule {
  std::string attribute;
  std::vector<ScoreRange> ranges;
};

struct DecisionBand {
  int min = 0;
  int max = 0;
  std::string decision;
  // empty means omit reason from output
  std::string reason;
};

struct ReturnRequest {
  std::string request_id;
  std::string account_id;
  std::string category;
  int days_since_purchase = 0;
  double order_value_usd = 0.0;
  int account_age_days = 0;
};

struct RoutingResult {
  std::string request_id;
  // -1 means JSON null
  int risk_score = -1;
  std::string decision;
  std::string reason;
};

class Engine {
 public:
  static Engine build(
      const std::vector<CategoryRule>& categories,
      const std::vector<ScoringRule>& scoring_rules,
      const std::vector<DecisionBand>& decision_bands,
      const std::unordered_map<std::string, int>& account_profiles,
      const std::vector<AccountLink>& links);

  RoutingResult route(const ReturnRequest& request) const;
  nlohmann::json to_json(const RoutingResult& result) const;

 private:
  std::unordered_map<std::string, CategoryRule> categories_;
  std::vector<ScoringRule> scoring_rules_;
  std::vector<DecisionBand> decision_bands_;
  std::unordered_map<std::string, int> account_profiles_;
  // account_id -> full linked group (including self after closure helpers)
  std::unordered_map<std::string, std::unordered_set<std::string>> account_groups_;

  int linked_return_history(const std::string& account_id) const;
  int score_request(const ReturnRequest& request, int return_history_count) const;
  const DecisionBand* band_for(int score) const;
};

}  // namespace returns
