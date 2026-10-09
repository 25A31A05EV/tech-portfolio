import heapq


class Solution:

    def minInterval(
        self,
        intervals: list[list[int]],
        queries: list[int]
    ) -> list[int]:

        # Sort intervals by starting point
        intervals.sort()

        # Sort queries while preserving their original indexes
        sorted_queries = sorted(
            (q, i) for i, q in enumerate(queries)
        )

        # Initialize answers with -1
        ans = [-1] * len(queries)

        # Min heap stores (interval_length, end)
        heap = []

        # Pointer to the next interval
        i = 0

        for q, original_index in sorted_queries:

            # Add intervals that have started
            while (
                i < len(intervals)
                and intervals[i][0] <= q
            ):
                start, end = intervals[i]

                length = end - start + 1

                heapq.heappush(heap, (length, end))

                i += 1

            # Remove intervals that end before the query
            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            # The heap top is the shortest valid interval
            if heap:
                ans[original_index] = heap[0][0]

        return ans