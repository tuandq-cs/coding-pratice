from heapq import heappop, heappush
from typing import List


class Solution:
    # https://leetcode.com/problems/minimum-cost-to-hire-k-workers/solutions/141768/detailed-explanation-o-nlogn/comments/148422
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        # expected = wage / quality
        # sort expected
        # cost[i] = quality[i] * expected[k], k is the last worker that has max expected in the group
        # => total cost = expected[k] * sum(quality[i])
        # try the next k: k + 1 => expected[k+1] >= expected[k]
        # then we need to decrease the worker has most quality in the group, to reduce the cost
        n = len(quality)
        expected = sorted([(wage[i]/quality[i], quality[i]) for i in range(n)])
        h = []
        sumQ = 0
        for i in range(k):
            _, q = expected[i]
            sumQ += q
            heappush(h, -q) # max heap
        cost = sumQ * expected[k-1][0]
        for i in range(k, n):
            # remove the worker has most quality
            removeQ = heappop(h)
            removeQ = -removeQ
            sumQ -= removeQ
            # add new worker at current i
            exp, newQ = expected[i]
            sumQ += newQ
            cost = min(cost, sumQ * exp)
            heappush(h, -newQ)
        return cost

