"""
Day 76 - Longest Common Subsequence
LeetCode 1143

Pattern: Dynamic Programming + Memoization

Problem:
Given two strings, find the length of their longest common subsequence.

A subsequence keeps the original order of characters,
but the characters do not need to be next to each other.

Example:
text1 = "abcde"
text2 = "ace"

Longest Common Subsequence = "ace"
Answer = 3

Approach:
1. Compare characters at positions i and j.
2. If they are equal:
       Take that character.
       Answer = 1 + remaining problem.
3. If they are different:
       Skip the character from text1
       OR
       Skip the character from text2.
       Take the maximum of both choices.
4. Use memoization so the same (i, j) state is not
   calculated repeatedly.

Time Complexity: O(m * n)
Space Complexity: O(m * n)
"""

from functools import lru_cache


class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # dp(i, j) means:
        # LCS length between text1[i:] and text2[j:]
        @lru_cache(None)
        def dp(i, j):

            # Base case:
            # If either string has reached its end,
            # no more common characters are possible.
            if i == len(text1) or j == len(text2):
                return 0

            # Case 1:
            # Current characters are equal.
            # Include the character and move both pointers.
            if text1[i] == text2[j]:
                return 1 + dp(i + 1, j + 1)

            # Case 2:
            # Current characters are different.
            #
            # Option 1:
            # Skip the current character from text1.
            skip_text1 = dp(i + 1, j)

            # Option 2:
            # Skip the current character from text2.
            skip_text2 = dp(i, j + 1)

            # Take the better result.
            return max(skip_text1, skip_text2)

        # Start from the beginning of both strings.
        return dp(0, 0)