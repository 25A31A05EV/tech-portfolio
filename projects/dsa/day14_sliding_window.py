"""
Day 14 - Sliding Window

Problems:
1. Maximum Sum Subarray of Size K
2. LeetCode 1456 - Maximum Number of Vowels in a Substring of Given Length
3. LeetCode 209 - Minimum Size Subarray Sum

Time Complexity:
1. O(n)
2. O(n)
3. O(n)

Space Complexity:
O(1)
"""

from typing import List

# --------------------------------------------------
# 1. Maximum Sum Subarray of Size K
# --------------------------------------------------

def max_sum_subarray(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)

    return max_sum


arr = [2, 1, 5, 1, 3, 2]
k = 3

print("Maximum Sum:", max_sum_subarray(arr, k))


# --------------------------------------------------
# 2. LeetCode 1456
# Maximum Number of Vowels in a Substring
# --------------------------------------------------

class MaxVowelsSolution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        window_count = 0

        # First window
        for i in range(k):
            if s[i] in vowels:
                window_count += 1

        max_count = window_count

        # Slide the window
        for i in range(k, len(s)):
            if s[i - k] in vowels:
                window_count -= 1

            if s[i] in vowels:
                window_count += 1

            max_count = max(max_count, window_count)

        return max_count


obj = MaxVowelsSolution()
print("Maximum Vowels:", obj.maxVowels("abciiidef", 3))


# --------------------------------------------------
# 3. LeetCode 209
# Minimum Size Subarray Sum
# --------------------------------------------------

class MinSubArraySolution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        window_sum = 0
        min_len = float('inf')

        for right in range(len(nums)):
            window_sum += nums[right]

            while window_sum >= target:
                min_len = min(min_len, right - left + 1)
                window_sum -= nums[left]
                left += 1

        if min_len == float('inf'):
            return 0

        return min_len


obj = MinSubArraySolution()
print("Minimum Length:", obj.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))