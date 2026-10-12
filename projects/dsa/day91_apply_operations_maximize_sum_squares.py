from typing import List


class Solution:

    def maxSum(self, A: List[int], k: int) -> int:

        count = [0] * 35

        # Count how many numbers contain each bit
        for a in A:
            for i in range(35):
                if a & (1 << i):
                    count[i] += 1

        res = 0
        mod = 10**9 + 7

        # Construct k numbers with the largest possible values
        for _ in range(k):
            cur = 0

            for i in range(35):
                if count[i] > 0:
                    count[i] -= 1
                    cur += 1 << i

            res = (res + cur * cur) % mod

        return res