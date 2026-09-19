"""
LeetCode 152: Maximum Product Subarray
Pattern: Dynamic Programming / Kadane's Algorithm

Given an integer array nums, find a subarray
that has the largest product and return the product.

A subarray:
- Must be contiguous.
- Must contain at least one number.

Example:
nums = [2, 3, -2, 4]
Answer = 6
"""

def max_product(nums):
    current_max = nums[0]
    current_min = nums[0]
    result = nums[0]

    for num in nums[1:]:
        if num < 0:
            current_max, current_min = current_min, current_max

        current_max = max(num, current_max * num)
        current_min = min(num, current_min * num)

        result = max(result, current_max)

    return result


# Test cases
print(max_product([2, 3, -2, 4]))       # 6
print(max_product([-2, 0, -1]))         # 0
print(max_product([-2, 3, -4]))         # 24
print(max_product([2, -5, -2, -4, 3]))  # 24