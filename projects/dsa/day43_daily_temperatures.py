"""
LeetCode 739: Daily Temperatures
Pattern: Stack (Monotonic Stack)

Given an array of daily temperatures, return an array where
answer[i] is the number of days you have to wait after day i
to get a warmer temperature. If there is no future day for
which this is possible, put 0.
"""

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []  # stores indices of days waiting for a warmer day

        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                j = stack.pop()
                result[j] = i - j

            stack.append(i)

        return result


# Test cases
sol = Solution()
print(sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
# Output: [1,1,4,2,1,1,0,0]

print(sol.dailyTemperatures([30, 40, 50, 60]))
# Output: [1,1,1,0]

print(sol.dailyTemperatures([30, 60, 90]))
# Output: [1,1,0]