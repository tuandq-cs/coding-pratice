from typing import List
import math

class Solution:
    def hourEatAll(self, piles: List[int], k: int) -> int:
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / k)
        return hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = r
        while (l <= r):
            m = l + (r - l) // 2
            if self.hourEatAll(piles, m) <= h:
                k = m
                r = m - 1
            else:
                l = m + 1
        return k
        # Time: O(n*log(max(piles[i])))
    
piles = [3,6,7,11]
h = 8
# l = 4, r = 3
# m = 3
# k = 4
# hours += 1 + 2 + 3 + 4 = 10
piles = [30,11,23,4,20]
h = 5
# l = 30, r = 30
# m = 30
# k = 30
# hours += 1 + 1 + 1 + 1 + 1 = 5

piles = [30,11,23,4,20]
h = 6
# l = 20, r = 22
# m = 19
# k = 23
# hours = 2 + 1 + 2 + 1 + 2 = 8

# edges
# one element
piles = [30]
h = 2
out = Solution().minEatingSpeed(piles, h)
print(out)
