"""
LeetCode 153: Find Minimum in Rotated Sorted Array
Pattern: Binary Search (Rotated/Modified Arrays)

Given a rotated sorted array with no duplicates, find the minimum element.
Must run in O(log n) time.
"""

def findMin(nums):
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    
    return nums[left]


# Test cases
print(findMin([4, 5, 6, 7, 0, 1, 2]))  # Output: 0
print(findMin([3, 4, 5, 1, 2]))        # Output: 1
print(findMin([1]))                     # Output: 1
print(findMin([2, 1]))                  # Output: 1