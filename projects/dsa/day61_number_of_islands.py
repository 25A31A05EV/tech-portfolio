"""
LeetCode 200: Number of Islands
Pattern: Graph + Matrix Traversal (DFS)

Given an m x n 2D binary grid which represents a map of '1's
(land) and '0's (water), return the number of islands. An
island is surrounded by water and is formed by connecting
adjacent lands horizontally or vertically.
"""

def numIslands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()

    def dfs(r, c):
        if (r < 0 or r >= rows or c < 0 or c >= cols or
                grid[r][c] == "0" or (r, c) in visited):
            return
        visited.add((r, c))
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    islands = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                dfs(r, c)
                islands += 1

    return islands


# Test case
grid = [
    ["1", "1", "0", "0"],
    ["1", "1", "0", "0"],
    ["0", "0", "1", "0"],
    ["0", "0", "0", "1"]
]
print(numIslands(grid))
# Output: 3

# Time: O(rows * cols) - each cell visited once
# Space: O(rows * cols) - visited set, worst case (+ recursion stack)