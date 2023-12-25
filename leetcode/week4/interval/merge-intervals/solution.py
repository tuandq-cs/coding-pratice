from typing import List


def isOverlap(firstInterval: List[List[int]], secondInterval: List[List[int]]) -> bool:
    return secondInterval[0] <= firstInterval[1]


def merge2Intervals(firstInterval: List[List[int]], secondInterval: List[List[int]]) -> List[List[int]]:
    return [min(firstInterval[0], secondInterval[0]), max(firstInterval[1], secondInterval[1])]


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        out = []
        prevInterval = intervals[0]
        for interval in intervals:
            if isOverlap(prevInterval, interval):
                prevInterval = merge2Intervals(prevInterval, interval)
                continue
            out.append(prevInterval)
            prevInterval = interval
        out.append(prevInterval)
        return out


intervals = [[8, 10], [15, 18], [1, 3], [2, 6]]
out = Solution().merge(intervals)
print(out)


# Corner cases

# Duplicate intervals
intervals = [[1, 2], [1, 2]]
out = Solution().merge(intervals)
print(out)

# Contained intervals
intervals = [[1, 5], [2, 3]]
out = Solution().merge(intervals)
print(out)

# One interval
intervals = [[1, 5]]
out = Solution().merge(intervals)
print(out)
