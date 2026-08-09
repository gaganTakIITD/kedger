#include "engine.h"

#include <cassert>
#include <iostream>
#include <vector>

using namespace returns;

static void test_bidirectional_links_include_related_account_history() {
    Engine engine;

    std::vector<CategoryRule> categories = {
        {"ELECTRONICS", true, 30},
    };

    std::vector<ScoringRule> scoring = {
        {"total_return_history",
         {{0, 2, 0}, {3, 7, 20}, {8, 1000000, 40}}},
    };

    std::vector<AccountProfile> profiles = {
        {"u201", 1},
        {"u202", 6},
    };

    // Link is stored one-way in input: u201 -> u202
    std::vector<AccountLink> links = {
        {"u201", "u202", "SHARED_SHIPPING_ADDRESS"},
    };

    engine.build(categories, scoring, profiles, links);

    ReturnRequest request;
    request.request_id = "r-test";
    request.account_id = "u202";
    request.category = "ELECTRONICS";
    request.days_since_purchase = 5;
    request.order_value_usd = 100;
    request.account_age_days = 200;

    const ReturnResult result = engine.process(request);

    // u202 should see u201's history (1 + 6 = 7) => 20 points => MANUAL_REVIEW
    assert(result.risk_score.has_value());
    assert(*result.risk_score == 20);
    assert(result.decision == "AUTO_APPROVE");
}

static void test_category_reject_has_null_score() {
    Engine engine;
    engine.build({{"GROCERY", false, 0}}, {}, {}, {});

    ReturnRequest request;
    request.request_id = "r-grocery";
    request.account_id = "u1";
    request.category = "GROCERY";
    request.days_since_purchase = 1;
    request.order_value_usd = 10;
    request.account_age_days = 100;

    const ReturnResult result = engine.process(request);
    assert(!result.risk_score.has_value());
    assert(result.decision == "REJECT");
    assert(result.reason == "RETURN_WINDOW_EXPIRED" || result.reason == "CATEGORY_NON_RETURNABLE");
}

int main() {
    test_bidirectional_links_include_related_account_history();
    test_category_reject_has_null_score();
    std::cout << "All tests passed\n";
    return 0;
}
