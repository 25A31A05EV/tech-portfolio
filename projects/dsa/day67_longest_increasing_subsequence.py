"""
LeetCode 300: Longest Increasing Subsequence
Pattern: Dynamic Programming (1D DP)

Given an integer array nums, return the length of the
longest strictly increasing subsequence.

A subsequence:
- Maintains the original order of elements.
- Does not need to contain consecutive elements.
- Must be strictly increasing.

Example:
nums = [10, 9, 2, 5, 3, 7, 101, 18]

Longest increasing subsequence:
[2, 3, 7, 101]

So the answer is 4.


Key idea:
dp[i] = length of the longest increasing subsequence
        that ends at index i.

Initially:
dp[i] = 1

Because every element by itself is an increasing
subsequence of length 1.


For every index i, we check all previous indices j.

If:
    nums[j] < nums[i]

then nums[i] can be added after nums[j].

So:
    dp[i] = max(dp[i], dp[j] + 1)


Important:
We use j < i because a subsequence must maintain
the original order of the array.


Example:

nums = [2, 3, 7]

Initially:
dp = [1, 1, 1]

For 3:
2 < 3
dp[1] = max(1, dp[0] + 1)
      = max(1, 2)
      = 2

For 7:
2 < 7
dp[2] = max(1, dp[0] + 1)
      = 2

3 < 7
dp[2] = max(2, dp[1] + 1)
      = 3

Final:
dp = [1, 2, 3]

Answer = max(dp) = 3
"""


def lengthOfLIS(nums):
    n = len(nums)

    # Every element itself forms a subsequence of length 1
    dp = [1] * n

    # i = current element
    for i in range(n):

        # j = previous elements
        for j in range(i):

            # Check whether the sequence can be extended
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


# Test cases

print(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
# Output: 4
# Longest increasing subsequence:
# [2, 3, 7, 101]


print(lengthOfLIS([0, 1, 0, 3, 2, 3]))
# Output: 4
# One longest increasing subsequence:
# [0, 1, 2, 3]


print(lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))
# Output: 1
# No two elements are strictly increasing


print(lengthOfLIS([3, 2, 1]))
# Output: 1
# The array is decreasing, so only one element can be chosen


print(lengthOfLIS([1, 2, 3, 4, 5]))
# Output: 5
# The complete array is increasing


# Time: O(n²)
# Space: O(n) - dp array