# Day 72 - DSA #73
# LeetCode 416 - Partition Equal Subset Sum
# Pattern: 0/1 Knapsack + 1D DP


def canPartition(nums):
    total = sum(nums)

    # If total is odd, equal partition is impossible
    if total % 2 != 0:
        return False

    target = total // 2

    # dp[t] = can we make sum t?
    dp = [False] * (target + 1)
    dp[0] = True

    # Process each number once
    for num in nums:
        # Move backward for 0/1 Knapsack
        for t in range(target, num - 1, -1):
            dp[t] = dp[t] or dp[t - num]

    return dp[target]


# Test cases
print(canPartition([1, 5, 11, 5]))  # True
print(canPartition([1, 2, 3, 5]))   # False