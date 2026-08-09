#include "engine.hpp"

#include <fstream>
#include <iostream>
#include <sstream>
#include <string>

using json = nlohmann::json;
using returns::AccountLink;
using returns::CategoryRule;
using returns::DecisionBand;
using returns::Engine;
using returns::ReturnRequest;
using returns::ScoringRule;

namespace {

std::string read_file(const std::string& path) {
  std::ifstream in(path);
  if (!in) {
    throw std::runtime_error("failed to open " + path);
  }
  std::ostringstream ss;
  ss << in.rdbuf();
  return ss.str();
}

std::vector<json> read_jsonl(const std::string& path) {
  std::ifstream in(path);
  if (!in) {
    throw std::runtime_error("failed to open " + path);
  }
  std::vector<json> rows;
  std::string line;
  while (std::getline(in, line)) {
    if (line.empty()) {
      continue;
    }
    rows.push_back(json::parse(line));
  }
  return rows;
}

}  // namespace

int main(int argc, char** argv) {
  const std::string data_dir = argc > 1 ? argv[1] : "data";

  const json category_doc =
      json::parse(read_file(data_dir + "/category_rules.json"));
  const json scoring_doc =
      json::parse(read_file(data_dir + "/scoring_rules.json"));
  const json bands_doc =
      json::parse(read_file(data_dir + "/decision_bands.json"));

  std::vector<CategoryRule> categories;
  for (const auto& item : category_doc.at("categories")) {
    CategoryRule rule;
    rule.category = item.at("category").get<std::string>();
    rule.returnable = item.at("returnable").get<bool>();
    rule.allowed_return_window_days =
        item.at("allowed_return_window_days").get<int>();
    categories.push_back(rule);
  }

  std::vector<ScoringRule> scoring_rules;
  for (const auto& item : scoring_doc.at("rules")) {
    ScoringRule rule;
    rule.attribute = item.at("attribute").get<std::string>();
    for (const auto& r : item.at("ranges")) {
      rule.ranges.push_back(
          {r.at("min").get<int>(), r.at("max").get<int>(),
           r.at("points").get<int>()});
    }
    scoring_rules.push_back(rule);
  }

  std::vector<DecisionBand> bands;
  for (const auto& item : bands_doc.at("bands")) {
    DecisionBand band;
    band.min = item.at("min").get<int>();
    band.max = item.at("max").get<int>();
    band.decision = item.at("decision").get<std::string>();
    if (!item.at("reason").is_null()) {
      band.reason = item.at("reason").get<std::string>();
    }
    bands.push_back(band);
  }

  std::unordered_map<std::string, int> profiles;
  for (const auto& row : read_jsonl(data_dir + "/account_profiles.jsonl")) {
    profiles[row.at("account_id").get<std::string>()] =
        row.at("return_history_count").get<int>();
  }

  std::vector<AccountLink> links;
  for (const auto& row : read_jsonl(data_dir + "/account_links.jsonl")) {
    AccountLink link;
    link.primary_account_id = row.at("primary_account_id").get<std::string>();
    link.related_account_id = row.at("related_account_id").get<std::string>();
    link.link_type = row.value("link_type", "");
    links.push_back(link);
  }

  Engine engine =
      Engine::build(categories, scoring_rules, bands, profiles, links);

  std::ofstream out(data_dir + "/results.jsonl");
  if (!out) {
    throw std::runtime_error("failed to open results.jsonl for write");
  }

  for (const auto& row : read_jsonl(data_dir + "/requests.jsonl")) {
    ReturnRequest req;
    req.request_id = row.at("request_id").get<std::string>();
    req.account_id = row.at("account_id").get<std::string>();
    req.category = row.at("category").get<std::string>();
    req.days_since_purchase = row.at("days_since_purchase").get<int>();
    req.order_value_usd = row.value("order_value_usd", 0.0);
    req.account_age_days = row.value("account_age_days", 0);

    const auto result = engine.route(req);
    const json line = engine.to_json(result);
    out << line.dump() << "\n";
    std::cout << line.dump() << "\n";
  }

  return 0;
}
