class Solution:
    def findClosestElements(
        self, arr: list[int], k: int, x: int
    ) -> list[int]:

        left = 0
        right = len(arr) - k

        while left < right:
            mid = left + (right - left) // 2

            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left:left + k]