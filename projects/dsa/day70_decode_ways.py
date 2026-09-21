"""
LeetCode 91: Decode Ways
Pattern: 1D Dynamic Programming (DP)

Given a string containing digits, return the number of ways
to decode it using:
1 -> A
2 -> B
...
26 -> Z
"""


def numDecodings(s):
    # Invalid if empty or starts with 0
    if not s or s[0] == '0':
        return 0

    n = len(s)

    # dp[i] = number of ways to decode first i characters
    dp = [0] * (n + 1)

    # Base cases
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1):

        # Check one-digit decoding
        one_digit = s[i - 1]

        if one_digit != '0':
            dp[i] += dp[i - 1]

        # Check two-digit decoding
        two_digit = s[i - 2:i]

        if '10' <= two_digit <= '26':
            dp[i] += dp[i - 2]

    return dp[n]


# Example 1
s = "226"
print(numDecodings(s))  # Output: 3

# Example 2
s = "12"
print(numDecodings(s))  # Output: 2

# Example 3
s = "06"
print(numDecodings(s))  # Output: 0