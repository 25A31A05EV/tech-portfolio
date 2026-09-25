# Day 73 - DSA #74
# LeetCode 213 - House Robber II
# Pattern: 1D DP + Circular DP


class Solution:

    def _rob_linear(self, nums: list[int]) -> int:
        pr1, pr2 = 0, 0

        for m in nums:
            current = max(pr1, m + pr2)
            pr2 = pr1
            pr1 = current

        return pr1

    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # Case 1: Skip first house
        case1 = self._rob_linear(nums[1:])

        # Case 2: Skip last house
        case2 = self._rob_linear(nums[:-1])

        return max(case1, case2)


# Test cases
solution = Solution()

print(solution.rob([2, 3, 2]))        # 3
print(solution.rob([1, 2, 3, 1]))     # 4
print(solution.rob([2, 7, 9, 3, 1]))  # 11