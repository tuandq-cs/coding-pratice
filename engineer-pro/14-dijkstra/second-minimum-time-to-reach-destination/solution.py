import heapq
import math
from typing import List


class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        # 1st min, 2nd min
        dis = [[math.inf, math.inf] for _ in range(n)]
        dis[0][0] = 0

        adjList = [[] for _ in range(n)]
        for u, v in edges:
            u -= 1
            v -= 1
            adjList[u].append(v)
            adjList[v].append(u)
        pq = []
        heapq.heappush(pq, (0, 0))
        while (len(pq) != 0):
            du, u = heapq.heappop(pq)
            for v in adjList[u]:
                dv = self.getTime(du, change) + time
                if dv < dis[v][0]:
                    dis[v][1] = dis[v][0]
                    dis[v][0] = dv
                    heapq.heappush(pq, (dv, v))
                elif dis[v][0] < dv < dis[v][1]:
                    dis[v][1] = dv
                    heapq.heappush(pq, (dv, v))
        return dis[n-1][1]
                
    def getTime(self, t, change):
        if (t // change) % 2:
            return (t // change) * change + change
        return t
    
n = 5
edges = [[1,2],[1,3],[1,4],[3,4],[4,5]]
time = 3
change = 5
out = Solution().secondMinimum(n, edges, time, change)
print(out)