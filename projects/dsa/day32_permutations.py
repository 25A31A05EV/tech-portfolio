from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(current):
            if len(current) == len(nums):
                result.append(current[:])
                return

            for num in nums:
                if num not in current:
                    current.append(num)
                    backtrack(current)
                    current.pop()

        backtrack([])
        return result


# Example
nums = [1, 2, 3]
solution = Solution()

print(solution.permute(nums))