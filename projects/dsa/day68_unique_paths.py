"""
LeetCode 62: Unique Paths
Pattern: Dynamic Programming (2D Grid DP)

A robot is placed at the top-left corner of an m x n grid.

The robot can move only:
- Right
- Down

Return the number of unique paths from the top-left
corner to the bottom-right corner.


Example:

m = 3
n = 3

DP Grid:

1  1  1
1  2  3
1  3  6

Answer = 6


Key idea:
dp[i][j] = number of unique paths to reach cell (i, j).

To reach (i, j), the robot can come from:

1. Top  -> (i - 1, j)
2. Left -> (i, j - 1)

Therefore:

dp[i][j] = dp[i - 1][j] + dp[i][j - 1]


Base cases:

First row:
Only Right movement is possible.

So:
dp[0][j] = 1


First column:
Only Down movement is possible.

So:
dp[i][0] = 1
"""


def uniquePaths(m, n):

    # Create an m x n DP table
    dp = [[0] * n for _ in range(m)]

    # Fill the first row
    # Only Right movement is possible
    for j in range(n):
        dp[0][j] = 1

    # Fill the first column
    # Only Down movement is possible
    for i in range(m):
        dp[i][0] = 1

    # Fill the remaining cells
    for i in range(1, m):
        for j in range(1, n):

            # Top + Left
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    # Bottom-right cell contains the answer
    return dp[m - 1][n - 1]


# Test cases

print(uniquePaths(3, 7))
# Output: 28


print(uniquePaths(3, 2))
# Output: 3


print(uniquePaths(3, 3))
# Output: 6


print(uniquePaths(1, 5))
# Output: 1


print(uniquePaths(5, 1))
# Output: 1


# Time: O(m * n)
# Space: O(m * n)