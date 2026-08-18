"""
LeetCode 435: Non-overlapping Intervals
Pattern: Greedy + Merge Intervals family

Given an array of intervals, find the minimum number of intervals
you need to remove to make the rest of the intervals non-overlapping.
"""

def eraseOverlapIntervals(intervals):
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[1])
    count = 0
    prev_end = intervals[0][1]

    for start, end in intervals[1:]:
        if start < prev_end:
            count += 1
        else:
            prev_end = end

    return count


# Test cases
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
# Output: 1

print(eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
# Output: 2

print(eraseOverlapIntervals([[1,2],[2,3]]))
# Output: 0 (touching intervals, not overlapping)