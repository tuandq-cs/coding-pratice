from heapq import heappop, heappush
from typing import List


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        n = len(happiness)
        h = []
        for i in range(n):
            if len(h) == k and h[0] < happiness[i]:
                heappop(h)
            if len(h) < k:
                heappush(h, happiness[i])
        s = 0
        while (k > 0):
            v = heappop(h)
            s += max(v - (k-1), 0)
            k -= 1
        return s
