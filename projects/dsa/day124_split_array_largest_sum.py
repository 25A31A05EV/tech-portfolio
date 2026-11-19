class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)

        while left < right:
            capacity = left + (right - left) // 2

            subarrays = 1
            current_sum = 0

            for num in nums:
                if current_sum + num > capacity:
                    subarrays += 1
                    current_sum = 0

                current_sum += num

            if subarrays <= k:
                right = capacity
            else:
                left = capacity + 1

        return left