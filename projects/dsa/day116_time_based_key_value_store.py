from collections import defaultdict
from bisect import bisect_right

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.store.get(key, [])

        left, right = 0, len(values)

        while left < right:
            mid = left + (right - left) // 2

            if values[mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid

        return values[left - 1][1] if left > 0 else ""