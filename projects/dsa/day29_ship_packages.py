"""
LeetCode 1011: Capacity To Ship Packages Within D Days
Pattern: Binary Search on the Answer

Find the minimum ship capacity such that all packages
(in order) can be shipped within 'days' days.
"""

def shipWithinDays(weights, days):
    left, right = max(weights), sum(weights)

    while left < right:
        mid = (left + right) // 2

        days_needed = 1
        current_load = 0
        for w in weights:
            if current_load + w > mid:
                days_needed += 1
                current_load = 0
            current_load += w

        if days_needed <= days:
            right = mid
        else:
            left = mid + 1

    return left


# Test cases
print(shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5))   # Output: 15
print(shipWithinDays([3,2,2,4,1,4], 3))             # Output: 6
print(shipWithinDays([1,2,3,1,1], 4))               # Output: 3