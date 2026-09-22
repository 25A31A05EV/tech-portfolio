"""
LeetCode 377: Combination Sum IV
Pattern: 1D Dynamic Programming

Count the number of ordered combinations that add up to target.
Order matters.
"""


def combinationSum4(nums, target):
    # dp[t] = number of ways to make sum t
    dp = [0] * (target + 1)

    # Base case:
    # There is one way to make sum 0: choose nothing.
    dp[0] = 1

    for t in range(1, target + 1):
        for num in nums:
            if t - num >= 0:
                dp[t] += dp[t - num]

    return dp[target]


# Example 1
nums = [1, 2, 3]
target = 4

print(combinationSum4(nums, target))  # Output: 7


# Example 2
nums = [9]
target = 3

print(combinationSum4(nums, target))  # Output: 0