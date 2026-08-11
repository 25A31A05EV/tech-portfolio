"""
LeetCode 39: Combination Sum
Pattern: Backtracking (with repetition allowed)

Given distinct candidates and a target, find all unique combinations
where chosen numbers sum to target. Same number may be chosen multiple times.
"""

def combinationSum(candidates, target):
    result = []

    def backtrack(start, current, remaining):
        if remaining == 0:
            result.append(current[:])
            return
        if remaining < 0:
            return

        for i in range(start, len(candidates)):
            current.append(candidates[i])
            backtrack(i, current, remaining - candidates[i])
            current.pop()

    backtrack(0, [], target)
    return result


# Test cases
print(combinationSum([2, 3, 6, 7], 7))       # Output: [[2,2,3],[7]]
print(combinationSum([2, 3, 5], 8))          # Output: [[2,2,2,2],[2,3,3],[3,5]]
print(combinationSum([2], 1))                # Output: []