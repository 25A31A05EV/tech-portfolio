"""
LeetCode 875: Koko Eating Bananas
Pattern: Binary Search on the Answer

Koko must eat all banana piles within h hours.
Find the minimum eating speed k such that all piles finish within h hours.
"""

import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2
            hours = sum(math.ceil(pile / mid) for pile in piles)

            if hours <= h:
                right = mid
            else:
                left = mid + 1

        return left


# Test cases
sol = Solution()
print(sol.minEatingSpeed([3, 6, 7, 11], 8))   # Output: 4
print(sol.minEatingSpeed([30, 11, 23, 4, 20], 5))   # Output: 30
print(sol.minEatingSpeed([30, 11, 23, 4, 20], 6))   # Output: 23