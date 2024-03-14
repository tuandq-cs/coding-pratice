import heapq
import math
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        inf = 600001
        dis = [inf] * n
        adjList = [[] for _ in range(n)]
        for u, v, w in times:
            u -= 1
            v -= 1
            adjList[u].append((v, w))
        k -= 1
        dis[k] = 0
        pq = []
        heapq.heappush(pq, (0, k))
        while len(pq) != 0:
            _, u = heapq.heappop(pq)
            for v, w in adjList[u]:
                if dis[u] + w < dis[v]:
                    dis[v] = dis[u] + w
                    heapq.heappush(pq, (dis[v], v))
        m = max(dis)
        return -1 if m == inf else m