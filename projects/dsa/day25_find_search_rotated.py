"""
LeetCode 33: Search in Rotated Sorted Array
Pattern: Binary Search (Rotated/Modified Arrays)

Given a rotated sorted array (no duplicates) and a target value,
return its index, or -1 if not found. Must run in O(log n) time.
"""

def search(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        if nums[left] <= nums[mid]:  # left half is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # right half is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1


# Test cases
print(search([4,5,6,7,0,1,2], 0))   # Output: 4
print(search([4,5,6,7,0,1,2], 3))   # Output: -1
print(search([1], 0))                # Output: -1
print(search([5,1,3], 5))            # Output: 0