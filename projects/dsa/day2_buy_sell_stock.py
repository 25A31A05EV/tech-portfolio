# Day 2 - LeetCode #121: Best Time to Buy and Sell Stock
# Approach: One Pass | Time: O(n) | Space: O(1)

def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit

# Test
print(maxProfit([7, 1, 5, 3, 6, 4]))  # Output: 5
print(maxProfit([7, 6, 4, 3, 1]))     # Output: 0