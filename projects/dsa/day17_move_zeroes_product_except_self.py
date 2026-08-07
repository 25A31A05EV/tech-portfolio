# Day 17
# LeetCode 283: Move Zeroes
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def moveZeroes(self, nums):
        i = 0

        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1


# LeetCode 238: Product of Array Except Self
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n

        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n-1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer