class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        def findBound(find_first: bool) -> int:
            left = 0
            right = len(nums) - 1
            result = -1

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] == target:
                    result = mid

                    if find_first:
                        right = mid - 1
                    else:
                        left = mid + 1

                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return result

        first = findBound(True)
        last = findBound(False)

        return [first, last]