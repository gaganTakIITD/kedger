#include "engine.h"
#include "json_io.h"

#include <iostream>
#include <vector>

int main() {
    try {
        const auto category_rules = returns::io::loadCategoryRules("data/category_rules.json");
        const auto scoring_rules = returns::io::loadScoringRules("data/scoring_rules.json");
        const auto profiles = returns::io::loadAccountProfiles("data/account_profiles.jsonl");
        const auto links = returns::io::loadAccountLinks("data/account_links.jsonl");
        const auto requests = returns::io::loadReturnRequests("data/return_requests.jsonl");

        returns::Engine engine;
        engine.build(category_rules, scoring_rules, profiles, links);

        std::vector<returns::ReturnResult> results;
        results.reserve(requests.size());
        for (const auto& request : requests) {
            results.push_back(engine.process(request));
        }

        returns::io::writeResults("data/results.jsonl", results);
        return 0;
    } catch (const std::exception& ex) {
        std::cerr << ex.what() << '\n';
        return 1;
    }
}
