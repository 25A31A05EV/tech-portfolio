"""
Day 80: Regular Expression Matching
LeetCode 10

Approach:
Top-down Dynamic Programming + Memoization.

Symbols:
. -> matches any single character
* -> matches zero or more of the previous character

DP State:
dp(i, j) = whether s[i:] matches p[j:]

Key idea:
- Normal character / "." -> match and move both
- "x*" -> either skip x* or use x again
- Pattern finished -> string must also be finished

Time: O(m * n)
Space: O(m * n)
"""

from functools import lru_cache


class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        @lru_cache(None)
        def dp(i, j):

            # Pattern finished
            if j == len(p):
                return i == len(s)

            # Check current character match
            first_match = (
                i < len(s)
                and (s[i] == p[j] or p[j] == ".")
            )

            # Next pattern character is '*'
            if j + 1 < len(p) and p[j + 1] == "*":

                # 1. Skip x*
                # 2. Use x* for current character again
                return (
                    dp(i, j + 2)
                    or
                    (first_match and dp(i + 1, j))
                )

            # Normal character or '.'
            if first_match:
                return dp(i + 1, j + 1)

            return False


        return dp(0, 0)


# Example
if __name__ == "__main__":
    solution = Solution()

    s = "aa"
    p = "a*"

    print(solution.isMatch(s, p))
    # Expected output: True