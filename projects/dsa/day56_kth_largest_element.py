"""
LeetCode 215: Kth Largest Element in an Array
Pattern: Sorting (simple approach - Heap would be more optimal)

Given an integer array and an integer k, return the kth largest
element in the array.

Approach: sort the array, then the kth largest sits at index
(length - k), since sorting puts the smallest at index 0 and
the largest at the last index.

Note: this is O(n log n) because it fully sorts the array, which
is more work than necessary when only the top-k values are
needed. A Heap-based approach can do this in O(n log k) by
tracking only the top k values instead of ordering everything.
"""

from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]


# Test cases
sol = Solution()
print(sol.findKthLargest([3, 2, 1, 5, 6, 4], 2))
# Output: 5

print(sol.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
# Output: 4

print(sol.findKthLargest([1], 1))
# Output: 1

# Time: O(n log n) - due to sort(); a Heap approach could achieve O(n log k)
# Space: O(1) extra (excluding sort's internal space) if sorting in-place