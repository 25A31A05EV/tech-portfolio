"""
LeetCode 322: Coin Change
Pattern: Dynamic Programming (1D DP)

Given a list of coin denominations and an amount,
return the minimum number of coins needed to make that amount.

Each coin can be used unlimited times.

Example:
coins = [1, 2, 5], amount = 11

Best combination:
5 + 5 + 1 = 11
So the answer is 3.

Key idea:
dp[a] = minimum number of coins needed to make amount a.

We build the answer from smaller amounts to larger amounts.
For every amount, we try every coin.

If we use a coin:
    remaining amount = a - coin
    coins needed = dp[a - coin] + 1

Then we take the minimum:

    dp[a] = min(dp[a], dp[a - coin] + 1)

Base case:
dp[0] = 0
Because making amount 0 requires 0 coins.

If the target amount cannot be made,
dp[amount] remains infinity, so we return -1.
"""


def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for a in range(1, amount + 1):
        for coin in coins:
            if a - coin >= 0:
                dp[a] = min(dp[a], dp[a - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1


# Test cases

print(coinChange([1, 2, 5], 11))
# Output: 3
# Best combination: 5 + 5 + 1


print(coinChange([2], 3))
# Output: -1
# Impossible to make amount 3 using only coin 2


print(coinChange([1], 0))
# Output: 0
# No coins are needed to make amount 0


print(coinChange([2, 5, 10, 1, 3], 27))
# Output: 4
# Best combination: 10 + 10 + 5 + 2


# Time: O(amount * number of coins)
# Space: O(amount) - dp array