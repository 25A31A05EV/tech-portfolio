# Day 9: Merge Intervals

def merge_brute(intervals):
    """Brute Force - O(n^3) Worst Case"""

    intervals = sorted(intervals)

    merged = True

    while merged:
        merged = False

        for i in range(len(intervals)):
            for j in range(i + 1, len(intervals)):

                if intervals[i][1] >= intervals[j][0]:

                    intervals[i] = [
                        intervals[i][0],
                        max(intervals[i][1], intervals[j][1])
                    ]

                    intervals.pop(j)
                    merged = True
                    break

            if merged:
                break

    return intervals


def merge(intervals):
    """Optimal Solution - O(n log n)"""

    if not intervals:
        return []

    intervals.sort()

    result = [intervals[0]]

    for current in intervals[1:]:
        last = result[-1]

        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            result.append(current)

    return result


def merge_inplace(intervals):
    """Optimal In-place Solution - O(n log n), O(1) Extra Space"""

    if not intervals:
        return []

    intervals.sort()

    i = 0

    for j in range(1, len(intervals)):

        if intervals[j][0] <= intervals[i][1]:
            intervals[i][1] = max(intervals[i][1], intervals[j][1])

        else:
            i += 1
            intervals[i] = intervals[j]

    return intervals[:i + 1]


# Tests
intervals = [[1,3], [2,6], [8,10], [15,18]]

print("Brute Force:", merge_brute([i[:] for i in intervals]))
print("Optimal:", merge([i[:] for i in intervals]))
print("In-place:", merge_inplace([i[:] for i in intervals]))