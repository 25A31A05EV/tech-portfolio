"""
LeetCode 347: Top K Frequent Elements
Pattern: HashMap + Sorting

Given an integer array nums and an integer k, return the k most
frequent elements. You may return the answer in any order.
"""

from collections import Counter


def topKFrequent(nums, k):
    count = Counter(nums)
    sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)
    result = [item[0] for item in sorted_items[:k]]
    return result


# Test cases
print(topKFrequent([1, 1, 1, 2, 2, 3], 2))
# Output: [1, 2]

print(topKFrequent([1], 1))
# Output: [1]

print(topKFrequent([4, 4, 4, 5, 5, 6, 7], 1))
# Output: [4]

# Time: O(n log n) - due to sorting; a Heap could achieve O(n log k)
# Space: O(n) - for the Counter dictionary