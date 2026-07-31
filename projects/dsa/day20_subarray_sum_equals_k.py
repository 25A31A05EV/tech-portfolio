# Practice: Subarray Sum Equals K (different numbers)

def subarraySum(nums, k):
    count = 0
    curr_sum = 0
    prefix_sums = {0: 1}
    
    for num in nums:
        curr_sum += num
        if curr_sum - k in prefix_sums:
            count += prefix_sums[curr_sum - k]
        prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1
    
    return count


# Test
nums = [3, 4, 7, 2, -3, 1, 4, 2]
k = 7
print(subarraySum(nums, k))   # Output: 4