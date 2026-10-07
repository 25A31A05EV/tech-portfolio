class Solution:

    def maxSubarraySumCircular(self, nums: list[int]) -> int:

        total = 0

        current_max = 0
        max_sum = nums[0]

        current_min = 0
        min_sum = nums[0]

        for num in nums:

            # Kadane's algorithm for maximum subarray
            current_max = max(num, current_max + num)
            max_sum = max(max_sum, current_max)

            # Kadane's algorithm for minimum subarray
            current_min = min(num, current_min + num)
            min_sum = min(min_sum, current_min)

            # Calculate total sum
            total += num

        # If all numbers are negative
        if max_sum < 0:
            return max_sum

        # Circular maximum = total - minimum subarray
        circular_sum = total - min_sum

        return max(max_sum, circular_sum)