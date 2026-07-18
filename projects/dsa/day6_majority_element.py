# Day 6: Majority Element
# Two approaches - HashMap and Boyer-Moore Voting Algorithm

def majorityElement_hashmap(nums):
    """Approach 1: HashMap - O(n) time, O(n) space"""
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
    n = len(nums)
    for key, value in count.items():
        if value > n / 2:
            return key


def majorityElement_boyer_moore(nums):
    """Approach 2: Boyer-Moore Voting - O(n) time, O(1) space"""
    candidate = None
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1
    return candidate


# Test both approaches
nums = [2, 2, 1, 1, 1, 2, 2]
print("HashMap approach:", majorityElement_hashmap(nums))
print("Boyer-Moore approach:", majorityElement_boyer_moore(nums))