from typing import List
import heapq


class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        
        free = [] # heap: weight, index
        for i, w in enumerate(servers):
            heapq.heappush(free, (w, i))
        busy = [] # heap: finish, index
        i = 0
        t = 0
        ans = []
        while (i < len(tasks)):
            # server has finished task at time t
            while len(busy) != 0:
                finish, j = busy[0]
                if finish <= t:
                    heapq.heappop(busy)
                    heapq.heappush(free, (servers[j], j))
                else:
                    break
            if len(free) != 0:
                # assign tasks to free servers
                _, j = heapq.heappop(free)
                heapq.heappush(busy, (t + tasks[i], j))
                ans.append(j)
                i += 1
                t = max(t, i)
            else:
                # all servers are busy
                t = busy[0][0]
        return ans


servers = [3,3,2]
tasks = [1,2,3,2,1,2]

servers = [5,1,4,3,2]
tasks = [2,1,2,4,5,2,1]
out = Solution().assignTasks(servers, tasks)
print(out)
                    