import heapq
from multiprocessing import heap
from typing import List


class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        n, m = len(servers), len(tasks)
        iTask = 0
        t = 0
        free = [(w, i) for i, w in enumerate(servers)] # (weight, index) minHeap
        heapq.heapify(free)
        busy = [] # (freeAt, index) minHeap
        ans = []


        while (iTask < m):
            # free out those busy servers at time t
            while (len(busy) > 0 and busy[0][0] <= t):
                _, iServer = heapq.heappop(busy)
                heapq.heappush(free, (servers[iServer], iServer))
            # free servers is empty, need to jump to time of top busy server
            if len(free) == 0:
                t = busy[0][0]
            # assign tasks to free servers until there're no tasks
            while (iTask < m and iTask <= t and len(free) > 0):
                _, iServer = heapq.heappop(free)
                heapq.heappush(busy, (t + tasks[iTask], iServer))
                ans.append(iServer)
                iTask += 1
            t = max(t, iTask)
        return ans
        # Time: O(m*log(n)), Space: O(n) for busy + free, O(m) for ans