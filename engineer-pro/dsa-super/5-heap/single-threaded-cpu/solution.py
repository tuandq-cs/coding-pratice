from typing import List
import heapq


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks2 = []
        for i, task in enumerate(tasks):
            # enqueueTime, processingTime, index
            tasks2.append([task[0], task[1], i])
        tasks2 = sorted(tasks2) # Time: O(n*log(n))
        t = 0
        availableTasks = []
        i = 0
        ans = []
        while (i < len(tasks) or len(availableTasks) > 0):
            # already enqueue before t
            while (i < len(tasks) and tasks2[i][0] <= t):
                heapq.heappush(availableTasks, (tasks2[i][1], tasks2[i][2]))
                i += 1
            # idle at t and has available tasks
            if len(availableTasks):
                # chose one and process
                processingTime, idx = heapq.heappop(availableTasks)
                t += processingTime
                ans.append(idx)
            # idle at t and has no tasks
            else:
                # jump t to the next task
                t = tasks2[i][0]
        # Processing n tasks, each task will be pushed and pop from heap -> Time: O(n*log(n))
        return ans
        # Overall time complexity: O(n*log(n))
    
tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]
# t = 13
# i = 5
# availableTasks = [[7,4,3],[7,5,2],[7,10,0],[7,12,1]]
# ans = [4, 3, 2, 0, 1]

tasks = [[1,2],[2,4],[3,2],[4,1]]

out = Solution().getOrder(tasks)
print(out)
            