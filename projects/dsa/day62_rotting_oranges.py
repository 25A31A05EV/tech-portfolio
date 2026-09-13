"""
LeetCode 994: Rotting Oranges
Pattern: Graph (Multi-source BFS on grid)

Given a grid where 0=empty, 1=fresh orange, 2=rotten orange,
every minute any fresh orange adjacent to a rotten one becomes
rotten. Return the minimum number of minutes until no cell has
a fresh orange, or -1 if impossible.

Key difference from Number of Islands: instead of a single DFS
starting point, ALL rotten oranges start rotting simultaneously
(multi-source BFS), and we need to track TIME (minutes) - which
is naturally what BFS's level-by-level processing gives us,
just like Level Order Traversal on a tree.
"""

from collections import deque


def orangesRotting(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c))
            elif grid[r][c] == 1:
                fresh += 1

    minutes = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue and fresh > 0:
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc))
        minutes += 1

    return minutes if fresh == 0 else -1


# Test cases
print(orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
# Output: 4

print(orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
# Output: -1 (an isolated fresh orange can never rot)

print(orangesRotting([[0, 2]]))
# Output: 0 (no fresh oranges to begin with)

# Time: O(rows * cols) - each cell processed once
# Space: O(rows * cols) - queue, worst case