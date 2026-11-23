class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        left = 0
        right = 1

        # Step 1: Find a suitable search range.
        while reader.get(right) < target:
            right *= 2

        # Step 2: Binary search inside that range.
        while left <= right:
            mid = left + (right - left) // 2
            value = reader.get(mid)

            if value == target:
                return mid

            elif value < target:
                left = mid + 1

            else:
                right = mid - 1

        return -1