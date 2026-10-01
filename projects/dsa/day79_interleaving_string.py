"""
Day 79: Interleaving String
LeetCode 97

Approach:
Top-down Dynamic Programming + Memoization.

dp(i, j) means:
Can we form s3[i + j:] using s1[i:] and s2[j:]?

Key idea:
- s1[i] matches s3[i+j] → try taking from s1
- s2[j] matches s3[i+j] → try taking from s2
- If both match, try both using OR

Time: O(m * n)
Space: O(m * n)
"""

from functools import lru_cache


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        # All characters from s1 and s2 must be used
        if len(s1) + len(s2) != len(s3):
            return False

        @lru_cache(None)
        def dp(i, j):

            # Both strings are completely used
            if i == len(s1) and j == len(s2):
                return True

            k = i + j

            take_s1 = False
            take_s2 = False

            # Take character from s1
            if i < len(s1) and s1[i] == s3[k]:
                take_s1 = dp(i + 1, j)

            # Take character from s2
            if j < len(s2) and s2[j] == s3[k]:
                take_s2 = dp(i, j + 1)

            return take_s1 or take_s2

        return dp(0, 0)


# Example
if __name__ == "__main__":
    solution = Solution()

    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"

    print(solution.isInterleave(s1, s2, s3))