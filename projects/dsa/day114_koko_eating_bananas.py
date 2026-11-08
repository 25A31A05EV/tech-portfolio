class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            mid = left + (right - left) // 2

            hours = sum((pile + mid - 1) // mid for pile in piles)

            if hours <= h:
                right = mid
            else:
                left = mid + 1

        return left