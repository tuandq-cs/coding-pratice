from typing import List


class Solution:
    def findOverlapIntervals(self, intervals: List[List[int]], newInterval: List[int]):
        startIndex = endIndex = None
        for i, interval in enumerate(intervals):
            if min(interval[1], newInterval[1]) - max(interval[0], newInterval[0]) >= 0:
                if startIndex is None:
                    startIndex = i
                endIndex = i
        return startIndex, endIndex
    
    def merge(self, interval1: List[List[int]], interval2: List[List[int]]) -> List[List[int]]:
        return [min(interval1[0], interval2[0]), max(interval1[1], interval2[1])]

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        startIndex, endIndex = self.findOverlapIntervals(intervals, newInterval)
        if startIndex is not None:
            mergedInterval = self.merge(self.merge(intervals[startIndex], newInterval), intervals[endIndex])
            return intervals[:startIndex] + [mergedInterval] + intervals[endIndex+1:]
        for i, interval in enumerate(intervals):
            if newInterval[1] < interval[0]:
                return intervals[:i] + [newInterval] + intervals[i:]
        return intervals + [newInterval]
        # Time Complexity: O(n)

intervals = [[1,3],[6,9]]
newInterval = [2,5]
out = Solution().insert(intervals, newInterval)
print(out)

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
out = Solution().insert(intervals, newInterval)
print(out)

intervals = [[1,2],[6,7],[8,10],[12,16]]
newInterval = [3,5]
out = Solution().insert(intervals, newInterval)
print(out)

intervals = [[3,5],[6,7],[8,10],[12,16]]
newInterval = [1,2]
out = Solution().insert(intervals, newInterval)
print(out)

intervals = [[3,5],[6,7],[8,10],[12,16]]
newInterval = [17,20]
out = Solution().insert(intervals, newInterval)
print(out)

