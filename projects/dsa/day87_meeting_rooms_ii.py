import heapq


class Solution:

    def minMeetingRooms(self, intervals: list[list[int]]) -> int:

        if not intervals:
            return 0

        # Sort meetings by start time
        intervals.sort()

        # Min heap stores meeting end times
        heap = [intervals[0][1]]

        for start, end in intervals[1:]:

            # Reuse room if the earliest meeting has ended
            if heap[0] <= start:
                heapq.heappop(heap)

            # Add current meeting's end time
            heapq.heappush(heap, end)

        return len(heap)