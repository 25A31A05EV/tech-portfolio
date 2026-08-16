"""
LeetCode 57: Insert Interval
Pattern: Merge Intervals (Mock Interview Practice - Day 35)

Given a sorted list of non-overlapping intervals and a new interval,
insert the new interval and merge if necessary.
"""

def insert(intervals, newInterval):
    result = []
    i = 0
    n = len(intervals)

    # Part 1: add all intervals ending before newInterval starts
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1

    # Part 2: merge all overlapping intervals with newInterval
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    result.append(newInterval)

    # Part 3: add remaining intervals after newInterval
    while i < n:
        result.append(intervals[i])
        i += 1

    return result


# Test cases
print(insert([[1,3],[6,9]], [2,5]))
# Output: [[1,5],[6,9]]

print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
# Output: [[1,2],[3,10],[12,16]]