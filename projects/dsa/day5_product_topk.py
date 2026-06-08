# Day 5 - LeetCode #238: Product of Array Except Self
# Approach: Prefix & Suffix | Time: O(n) | Space: O(1)

def productExceptSelf(nums):
    n = len(nums)
    result = [1] * n

    # Left pass
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    # Right pass
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result

# Test
print(productExceptSelf([1, 2, 3, 4]))   # [24, 12, 8, 6]
print(productExceptSelf([-1, 1, 0, -3, 3]))  # [0, 0, 9, 0, 0]

# Day 5 - LeetCode #347: Top K Frequent Elements
# Approach: HashMap + Sort | Time: O(n log n) | Space: O(n)

def topKFrequent(nums, k):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1

    sorted_count = sorted(count, key=lambda x: count[x], reverse=True)
    return sorted_count[:k]

# Test
print(topKFrequent([1, 1, 1, 2, 2, 3], 2))  # [1, 2]
print(topKFrequent([1], 1))                   # [1]