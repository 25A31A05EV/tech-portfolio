"""
===========================================================
Day 78: Distinct Subsequences
LeetCode 115
===========================================================

Problem:
--------
Given two strings s and t, return the number of distinct
subsequences of s which equal t.

A subsequence:
----------------
A subsequence is formed by deleting some characters from
the original string without changing the relative order
of the remaining characters.

Example:
    s = "abcde"

Possible subsequences:
    "ace"  ✅
    "abc"  ✅
    "ae"   ✅
    "ca"   ❌  -> order is changed

Example:
--------
s = "rabbbit"
t = "rabbit"

Answer = 3

There are 3 different ways to choose characters from
"rabbbit" to form "rabbit".

-----------------------------------------------------------
Approach:
-----------------------------------------------------------

We use:
    Top-Down Dynamic Programming
    + Memoization

DP State:
----------
dp(i, j) means:

    Number of ways to form t[j:]
    using characters from s[i:].

where:
    i = current index in source string s
    j = current index in target string t

-----------------------------------------------------------
Main Logic:
-----------------------------------------------------------

1. Target is completely formed
--------------------------------

If:

    j == len(t)

then we have successfully formed the entire target.

There is exactly one valid way to complete this path.

So:

    return 1


2. Source is completely finished
---------------------------------

If:

    i == len(s)

but target is still not complete, there are no
characters left to form the target.

So:

    return 0


3. Characters are equal
-----------------------

If:

    s[i] == t[j]

we have TWO choices:

Choice 1: USE s[i]
    dp(i + 1, j + 1)

Choice 2: SKIP s[i]
    dp(i + 1, j)

Both choices can produce valid subsequences.

Therefore:

    dp(i, j) =
        dp(i + 1, j + 1)
        +
        dp(i + 1, j)


4. Characters are different
---------------------------

If:

    s[i] != t[j]

we cannot use s[i] to match t[j].

So we can only skip s[i]:

    dp(i + 1, j)

-----------------------------------------------------------
Important Memory Trick:
-----------------------------------------------------------

DISTINCT SUBSEQUENCES = COUNT WAYS

Same character:
    USE + SKIP -> ADD

Different character:
    SKIP

Target finished:
    1

Source finished:
    0

-----------------------------------------------------------
Why do we use ADD instead of MIN/MAX?
-----------------------------------------------------------

In Edit Distance:
    We wanted the minimum number of operations.
    So we used MIN.

In Distinct Subsequences:
    We want to COUNT all valid ways.
    So we ADD the possible ways.

-----------------------------------------------------------
Time Complexity:
-----------------------------------------------------------

Let:

    m = len(s)
    n = len(t)

There are at most:

    m * n

different DP states.

Because of @lru_cache, every state is computed only once.

Time:
    O(m * n)

-----------------------------------------------------------
Space Complexity:
-----------------------------------------------------------

The memoization cache can store up to:

    m * n

states.

The recursion stack can use O(m + n).

Overall:

    O(m * n)

-----------------------------------------------------------
Edge Cases:
-----------------------------------------------------------

1. t is empty
   Answer = 1

   Example:
       s = "abc"
       t = ""

   There is exactly one way to form an empty string:
   choose nothing.

2. s is empty but t is not
   Answer = 0

3. s is shorter than t
   Answer = 0

-----------------------------------------------------------
"""

from functools import lru_cache


class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        @lru_cache(None)
        def dp(i, j):
            """
            Return the number of ways to form t[j:]
            using characters from s[i:].
            """

            # ------------------------------------------------
            # Base Case 1:
            # Target is completely formed.
            # We found one valid subsequence.
            # ------------------------------------------------
            if j == len(t):
                return 1

            # ------------------------------------------------
            # Base Case 2:
            # Source is finished before target.
            # No characters are left to form the target.
            # ------------------------------------------------
            if i == len(s):
                return 0

            # ------------------------------------------------
            # Case 1:
            # Current characters are equal.
            #
            # We have two choices:
            #
            # 1. USE s[i]
            #    -> move both i and j
            #
            # 2. SKIP s[i]
            #    -> move only i
            #
            # Since we are counting ways, ADD both results.
            # ------------------------------------------------
            if s[i] == t[j]:
                use = dp(i + 1, j + 1)
                skip = dp(i + 1, j)

                return use + skip

            # ------------------------------------------------
            # Case 2:
            # Characters are different.
            #
            # s[i] cannot match t[j],
            # so we must SKIP s[i].
            # ------------------------------------------------
            return dp(i + 1, j)

        # Start from the first character of both strings.
        return dp(0, 0)


# ===========================================================
# Example 1
# ===========================================================

if __name__ == "__main__":

    solution = Solution()

    s = "rabbbit"
    t = "rabbit"

    answer = solution.numDistinct(s, t)

    print("Source string :", s)
    print("Target string :", t)
    print("Number of distinct subsequences :", answer)

    # Expected output:
    # Source string : rabbbit
    # Target string : rabbit
    # Number of distinct subsequences : 3


# ===========================================================
# Quick Revision
# ===========================================================

"""
DAY 78 QUICK REVISION:

dp(i, j)
    ↓
number of ways to form t[j:] from s[i:]

If target finished:
    return 1

If source finished:
    return 0

If s[i] == t[j]:
    USE + SKIP
    dp(i+1, j+1) + dp(i+1, j)

If s[i] != t[j]:
    SKIP
    dp(i+1, j)

Remember:

    Same      -> USE + SKIP -> ADD
    Different -> SKIP
    Target    -> 1
    Source    -> 0

Complexity:
    Time  = O(m * n)
    Space = O(m * n)
"""