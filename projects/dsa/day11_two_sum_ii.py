# Day 11: Two Sum II (Two Pointers)

def twoSum(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left + 1, right + 1]   # 1-based indexing
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return []


# Test
print(twoSum([2, 7, 11, 15], 9))        # Output: [1, 2]
print(twoSum([2, 3, 4], 6))             # Output: [1, 3]
print(twoSum([-1, 0], -1))              # Output: [1, 2]