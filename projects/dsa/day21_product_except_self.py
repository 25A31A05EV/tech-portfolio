# ==========================================
# Day 21 - Prefix Sum / Prefix-Suffix Pattern
# ==========================================

# ------------------------------------------
# 1. Running Sum of 1D Array
# ------------------------------------------

class RunningSumSolution:
    def runningSum(self, nums):
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums


# ------------------------------------------
# 2. Product of Array Except Self
# ------------------------------------------

class ProductExceptSelfSolution:
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n

        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer


# ------------------------------------------
# 3. Maximum Product Subarray
# ------------------------------------------

class MaximumProductSubarraySolution:
    def maxProduct(self, nums):
        max_prod = nums[0]
        min_prod = nums[0]
        ans = nums[0]

        for num in nums[1:]:
            if num < 0:
                max_prod, min_prod = min_prod, max_prod

            max_prod = max(num, max_prod * num)
            min_prod = min(num, min_prod * num)

            ans = max(ans, max_prod)

        return ans