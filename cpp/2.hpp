#include <vector>

namespace advent2024 {

enum class Trend { Increasing, Decreasing, Unset };

const std::vector<int> CopyWithIndexSkip(const std::vector<int>& arr, const int i);
bool TryWithTwoCandidates(const std::vector<int>& arr, const int i, const int skips_remaining);
bool IsSafe(const std::vector<int>& arr, const int skips_remaining);

}  // namespace advent2024
