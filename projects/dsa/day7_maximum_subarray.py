# Day 7: Maximum Subarray (Kadane's Algorithm)

def maxmum(nums):
    """Brute Force - O(n^2)"""
    n = len(nums)
    max_sum = float('-inf')
    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += nums[j]
            max_sum = max(curr_sum, max_sum)
    return max_sum


def maxmum2(nums):
    """Kadane's Algorithm - O(n)"""
    curr_sum = 0
    max_sum = float('-inf')
    for n in nums:
        curr_sum += n
        max_sum = max(curr_sum, max_sum)
        if curr_sum < 0:
            curr_sum = 0
    return max_sum


def maxmum3(nums):
    """Kadane's Algorithm with subarray indices - O(n)"""
    start = 0
    end = 0
    temp_start = 0
    curr_sum = 0
    max_sum = float('-inf')
    for i in range(len(nums)):
        curr_sum += nums[i]
        if curr_sum > max_sum:
            max_sum = curr_sum
            start = temp_start
            end = i
        if curr_sum < 0:
            curr_sum = 0
            temp_start = i + 1
    return max_sum, nums[start:end+1]


# Tests
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Brute Force:", maxmum(nums))
print("Kadane's:", maxmum2(nums))
print("Kadane's with indices:", maxmum3(nums))