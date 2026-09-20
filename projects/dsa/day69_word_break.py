"""
LeetCode 139: Word Break
Pattern: Dynamic Programming (1D DP)

Given a string s and a dictionary wordDict,
return True if s can be segmented into a
space-separated sequence of one or more
dictionary words.
"""


def wordBreak(s, wordDict):
    n = len(s)

    # dp[i] = True if s[0:i] can be segmented
    dp = [False] * (n + 1)

    # Empty string is breakable
    dp[0] = True

    for i in range(1, n + 1):
        for word in wordDict:

            if (
                i >= len(word)
                and dp[i - len(word)]
                and s[i - len(word):i] == word
            ):
                dp[i] = True
                break

    return dp[n]


# Example 1
s = "leetcode"
wordDict = ["leet", "code"]

print(wordBreak(s, wordDict))
# True


# Example 2
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]

print(wordBreak(s, wordDict))
# False