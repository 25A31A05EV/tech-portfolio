class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:

        left = max(weights)
        right = sum(weights)

        while left < right:
            capacity = left + (right - left) // 2

            required_days = 1
            current_load = 0

            for weight in weights:
                if current_load + weight > capacity:
                    required_days += 1
                    current_load = 0

                current_load += weight

            if required_days <= days:
                right = capacity
            else:
                left = capacity + 1

        return left