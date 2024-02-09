from typing import List
import heapq, math

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        h = []
        s = 0
        for p in piles:
            s += p
            heapq.heappush(h, -p)
        taken = 0
        for _ in range(k):
            p = heapq.heappop(h)
            p = -p
            taken += p // 2
            p = p - p // 2
            heapq.heappush(h, -p)
        return s - taken
    

piles = [5,4,9]
k = 2
# sum = 18
# h = (-5, -3, -4)
# taken = 6

piles = [4,3,6,7]
k = 3
out = Solution().minStoneSum(piles, k)
print(out)