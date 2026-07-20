# Day 8: Contains Duplicate

def contains_duplicate(nums):
    """Brute Force - O(n^2)"""
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    return False


def contains_duplicate2(nums):
    """Sorting - O(n log n)"""
    nums = sorted(nums)
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False


def contains_duplicate3(nums):
    """Hash Set - O(n)"""
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# Tests
nums1 = [1, 2, 3, 1]
nums2 = [1, 2, 3, 4]
nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

print("Brute Force:")
print(contains_duplicate(nums1))
print(contains_duplicate(nums2))
print(contains_duplicate(nums3))

print("\nSorting:")
print(contains_duplicate2(nums1))
print(contains_duplicate2(nums2))
print(contains_duplicate2(nums3))

print("\nHash Set:")
print(contains_duplicate3(nums1))
print(contains_duplicate3(nums2))
print(contains_duplicate3(nums3))