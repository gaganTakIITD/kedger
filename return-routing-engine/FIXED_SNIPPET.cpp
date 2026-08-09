// Minimal paste-in fix for the one-way link bug in Engine::build.
// Before (broken): only primary -> related was stored.
// After (correct): store both directions, then transitive-close.

std::unordered_map<std::string, std::unordered_set<std::string>> account_groups;

for (const auto& link : links) {
    account_groups[link.primary_account_id].insert(link.related_account_id);
    // FIX: linked accounts are an undirected group, not a directed arrow
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
            if (it != account_groups.end()) {
                for (const auto& transitive : it->second) {
                    if (transitive != id && expanded.find(transitive) == expanded.end()) {
                        expanded.insert(transitive);
                        changed = true;
                    }
                }
            }
        }
        group = std::move(expanded);
    }
}
