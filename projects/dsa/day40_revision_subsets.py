"""
LeetCode 78: Subsets (Revision — Day 40)
Pattern: Backtracking

Given an array of distinct integers, return all possible subsets
(the power set).

Revision note: Solved earlier on Day 30. Redone cold today to
reinforce the 3-step backtracking structure (Choose - Explore - Undo)
after this was identified as a weak area during Day 40 pattern revision.
"""

def subsets(nums):
    result = []
    current = []

    def backtrack(start):
        result.append(current[:])

        for i in range(start, len(nums)):
            current.append(nums[i])       # 1. choose
            backtrack(i + 1)              # 2. explore
            current.pop()                 # 3. undo

    backtrack(0)
    return result


# Test case
print(subsets([1, 2, 3]))
# Output: [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]