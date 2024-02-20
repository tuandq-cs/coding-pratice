from typing import List
import math

class Solution:
    def numTrips(self, time: List[int], atTime: int) -> int:
        trips = 0
        for t in time:
            trips += atTime // t
        return trips

    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l, r = 1, min(time) * totalTrips
        ans = r
        while (l <= r):
            m = l + (r - l) // 2
            if self.numTrips(time, m) >= totalTrips:
                ans = m
                r = m - 1
            else:
                l = m + 1
        return ans
        # Time: O(n*log(min(time[i]*totalTrips))), n is length of time
    
time = [1,2,3]
totalTrips = 5

time = [2]
totalTrips = 1

out = Solution().minimumTime(time, totalTrips)
print(out)