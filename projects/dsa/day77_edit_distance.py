"""
Day 77: Edit Distance
LeetCode 72

Problem:
Find the minimum number of operations required to convert word1 into word2.

Allowed operations:
1. Insert a character
2. Delete a character
3. Replace a character

Approach:
Top-down Dynamic Programming with Memoization.

DP State:
dp(i, j) = minimum number of operations needed to convert
word1[i:] into word2[j:].

Rules:
- If word1 is finished, insert all remaining characters of word2.
- If word2 is finished, delete all remaining characters of word1.
- If current characters are equal, move both pointers without cost.
- If they are different, try insert, delete, and replace,
  then take the minimum.

Time Complexity:
O(m * n)

Space Complexity:
O(m * n)

Example:
word1 = "horse"
word2 = "ros"

Answer = 3
"""

from functools import lru_cache


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        @lru_cache(None)
        def dp(i, j):
            # Base case:
            # word1 is completely processed.
            # We need to insert all remaining characters of word2.
            if i == len(word1):
                return len(word2) - j

            # Base case:
            # word2 is completely processed.
            # We need to delete all remaining characters of word1.
            if j == len(word2):
                return len(word1) - i

            # If characters are the same,
            # no operation is required.
            if word1[i] == word2[j]:
                return dp(i + 1, j + 1)

            # Characters are different.
            # Try all three operations.

            # 1. Insert:
            # Move j forward.
            insert = dp(i, j + 1)

            # 2. Delete:
            # Move i forward.
            delete = dp(i + 1, j)

            # 3. Replace:
            # Move both i and j forward.
            replace = dp(i + 1, j + 1)

            return 1 + min(insert, delete, replace)

        return dp(0, 0)


# Example usage:
if __name__ == "__main__":
    solution = Solution()

    word1 = "horse"
    word2 = "ros"

    result = solution.minDistance(word1, word2)

    print("Word 1:", word1)
    print("Word 2:", word2)
    print("Minimum operations:", result)