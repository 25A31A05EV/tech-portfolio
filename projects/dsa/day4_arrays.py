# Day 4 - LeetCode #217: Contains Duplicate
# Approach: HashSet | Time: O(n) | Space: O(n)

def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# Test
print(containsDuplicate([1, 2, 3, 1]))   # True
print(containsDuplicate([1, 2, 3, 4]))   # False

# Day 4 - LeetCode #53: Maximum Subarray
# Approach: Kadane's Algorithm | Time: O(n) | Space: O(1)

def maxSubArray(nums):
    max_sum = nums[0]
    current_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

# Test
print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
print(maxSubArray([1]))                                 # 1

# Day 4 - LeetCode #152: Maximum Product Subarray
# Approach: Track min & max | Time: O(n) | Space: O(1)

def maxProduct(nums):
    max_prod = nums[0]
    min_prod = nums[0]
    result = nums[0]

    for num in nums[1:]:
        candidates = (num, max_prod * num, min_prod * num)
        max_prod = max(candidates)
        min_prod = min(candidates)
        result = max(result, max_prod)

    return result

# Test
print(maxProduct([2, 3, -2, 4]))   # 6
print(maxProduct([-2, 0, -1]))     # 0