"""
LeetCode 70: Climbing Stairs
Pattern: Dynamic Programming (new pattern!) - Mock Interview #5

You are climbing a staircase with n steps. Each time you can
climb 1 or 2 steps. Return the number of distinct ways to
reach the top.

Key insight: to reach step n, the last move was either a
1-step (coming from n-1) or a 2-step (coming from n-2). So
ways(n) = ways(n-1) + ways(n-2) - this is the Fibonacci
sequence in disguise.

Base cases: ways(1)=1, ways(2)=2.

This is the space-optimized iterative version - instead of
storing the entire sequence in an array (O(n) space), only the
last two values are tracked (O(1) space), since that's all
that's needed to compute the next one.
"""


def climbStairs(n):
    if n <= 2:
        return n

    prev2, prev1 = 1, 2  # ways(1), ways(2)

    for i in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current

    return prev1


# Test cases
print(climbStairs(4))
# Output: 5

print(climbStairs(5))
# Output: 8

print(climbStairs(10))
# Output: 89

# Time: O(n) - single loop up to n
# Space: O(1) - only two variables tracked, no array or recursion stack