from heapq import heappop, heappush
from typing import List


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        h = []
        n = len(arr)
        for i in range(n-1):
            heappush(h, (arr[i]/arr[-1], i, n-1))
        for i in range(k-1):
            _, numIdx, deIdx = heappop(h)
            if numIdx < deIdx - 1:
                heappush(h, (arr[numIdx]/arr[deIdx-1], numIdx, deIdx-1))
        _, i, j = heappop(h)
        return [arr[i], arr[j]]