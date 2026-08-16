"""
LeetCode 131: Palindrome Partitioning
Pattern: Backtracking

Given a string s, partition it such that every substring
of the partition is a palindrome. Return all possible partitions.
"""

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def is_palindrome(sub):
            return sub == sub[::-1]

        def backtrack(start, current):
            if start == len(s):
                result.append(current[:])
                return
            for i in range(start, len(s)):
                substring = s[start:i+1]
                if is_palindrome(substring):
                    current.append(substring)
                    backtrack(i+1, current)
                    current.pop()

        backtrack(0, [])
        return result


# Test cases
sol = Solution()
print(sol.partition("aab"))   # [["a","a","b"],["aa","b"]]
print(sol.partition("a"))     # [["a"]]
print(sol.partition("aba"))   # [["a","b","a"],["aba"]]