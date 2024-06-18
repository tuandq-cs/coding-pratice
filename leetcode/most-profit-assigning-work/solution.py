from heapq import heappop, heappush
from typing import List


class Solution:
    def binarySearch(self, worker: List[int], l: int, diff: int) -> int:
        r = len(worker) - 1
        res = -1
        while (l <= r):
            m = l + (r - l) // 2
            if worker[m] >= diff: # want right most
                res = m
                l = m + 1
            else:
                r = m - 1
        return res

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # n jobs, each has diff[i], profit[i]
        # m workers, each worker can handle max diff = worker[j]
        # find max profit
        # max heap (profit, diff)
        # build max heap
        n = len(profit)
        maxH = []
        for i in range(n): # O(n*logn)
            p, d = profit[i], difficulty[i]
            heappush(maxH, (-p, d)) # python is maxHeap
        worker = sorted(worker, reverse=True)
        j = 0
        m = len(worker)
        # pop from job from maxHeap
        res = 0
        while (maxH and j < m): # worse case, every job (n), need to binarySearch whole worker array (log(m)) => O(nlogm)
            p, d = heappop(maxH)
            p = -p
            # binary search to find k workers can handle d
            k = self.binarySearch(worker, j, d)
            if k == -1:
                continue
            res += (k-j+1)*p
            j = k+1
        # Overall: Time: O(nlogn + nlogm), Space: O(n)
        return res