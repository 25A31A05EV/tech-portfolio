"""
LeetCode 56: Merge Intervals
Pattern: Merge Intervals

Given an array of intervals, merge all overlapping intervals,
and return an array of the non-overlapping intervals that
cover all the intervals in the input.
"""

class Solution:
    def merge(self, intervals):
        intervals.sort()

        result = []

        for interval in intervals:
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])

        return result


# Test cases
sol = Solution()
print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))
# Output: [[1,6],[8,10],[15,18]]

print(sol.merge([[1,4],[4,5]]))
# Output: [[1,5]]

print(sol.merge([[1,10],[2,3]]))
# Output: [[1,10]]  (nested interval edge case)