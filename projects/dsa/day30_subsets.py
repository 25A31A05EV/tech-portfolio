"""
LeetCode 78: Subsets
Pattern: Backtracking

Given an array of unique integers, return all possible subsets (the power set).
"""

def subsets(nums):
    result = []

    def backtrack(start, current):
        result.append(current[:])  # add a copy of current subset

        for i in range(start, len(nums)):
            current.append(nums[i])       # choose
            backtrack(i + 1, current)     # explore
            current.pop()                  # un-choose (backtrack)

    backtrack(0, [])
    return result


# Test
print(subsets([1, 2, 3]))
# Output: [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]
print(len(subsets([1, 2, 3])))  # Output: 8