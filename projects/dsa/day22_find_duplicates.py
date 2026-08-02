def findDuplicates(nums):
    result = []
    
    for i in range(len(nums)):
        num = abs(nums[i])
        index = num - 1
        
        if nums[index] < 0:
            result.append(num)
        else:
            nums[index] = -nums[index]
    
    return result


# Test
nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(findDuplicates(nums))   # Expected: [2, 3]