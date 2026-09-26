"""
LeetCode 494: Target Sum
Pattern: Dynamic Programming (DP)

You are given an integer array nums and an integer target.
For every number, you can choose either +num or -num.

Return the number of different ways to assign signs so that
the final sum equals target.

Key insight: At every number, there are two choices:
+num or -num.

dp[sum] = number of ways to reach that sum.

Start with:
dp = {0: 1}

For every number:
    new_sum = current_sum + num
    new_sum = current_sum - num

If multiple paths reach the same sum, add their ways.

We use new_dp because dp represents the previous state,
while new_dp represents the next state after using the
current number.

Example:
nums = [1, 1, 1]
target = 1

After first 1:
{1: 1, -1: 1}

After second 1:
{2: 1, 0: 2, -2: 1}

After third 1:
{3: 1, 1: 3, -1: 3, -3: 1}

Therefore:
dp[1] = 3

Time: O(n * S)
Space: O(S)

S = number of possible sums.
"""

from collections import defaultdict


class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        dp = {0: 1}

        for num in nums:
            new_dp = defaultdict(int)

            for current_sum, ways in dp.items():
                new_dp[current_sum + num] += ways
                new_dp[current_sum - num] += ways

            dp = new_dp

        return dp.get(target, 0)


# Test cases
print(Solution().findTargetSumWays([1, 1, 1], 1))
# Output: 3

print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3))
# Output: 5