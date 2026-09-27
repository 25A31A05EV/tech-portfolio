"""
LeetCode 55: Jump Game
Pattern: Greedy

You are given an integer array nums.
nums[i] tells us the maximum number of steps we can jump
forward from index i.

Return True if we can reach the last index.
Otherwise, return False.

Example:
nums = [2, 3, 1, 1, 4]

From index 0, we can reach up to index 2.
From index 1, we can reach up to index 4.

So the last index is reachable.

Key insight:
We do not need to try every possible path.

Instead, keep track of the farthest index that can be
reached so far.

For each reachable index:
    farthest = max(farthest, i + nums[i])

If i > farthest:
    the current index cannot be reached, so return False.

If farthest reaches the last index:
    return True.

Remember:
nums[i] = maximum jump length
i + nums[i] = farthest reach from index i
farthest = best reach found so far
"""


def canJump(nums: list[int]) -> bool:
    farthest = 0

    for i in range(len(nums)):

        # Current index cannot be reached
        if i > farthest:
            return False

        # Update the farthest reachable index
        farthest = max(farthest, i + nums[i])

        # We can already reach the last index
        if farthest >= len(nums) - 1:
            return True

    return True


# Test cases

print(canJump([2, 3, 1, 1, 4]))
# Output: True

print(canJump([3, 2, 1, 0, 4]))
# Output: False

print(canJump([2, 0, 0]))
# Output: True

print(canJump([0]))
# Output: True


# Time: O(n)
# We scan the array only once.

# Space: O(1)
# Only the farthest variable is used.