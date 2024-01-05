from typing import List


class Solution:
    def merge(self, interval1: List[List[int]], interval2: List[List[int]]) -> List[List[int]]:
        return [min(interval1[0], interval2[0]), max(interval1[1], interval2[1])]

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        r = []
        for i, interval in enumerate(intervals):
            if interval[0] > newInterval[1]:
                r.append(newInterval)
                return r + intervals[i:]
            if interval[1] < newInterval[0]:
                r.append(interval)
            else:
                newInterval = self.merge(newInterval, interval)
        r.append(newInterval)
        return r
        # Time: O(n)
    
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