from typing import List
import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        maxH = []
        usedBricks = 0
        i = 0
        while i < len(heights)-1:
            needBricks= heights[i+1] - heights[i]
            if needBricks <= 0:
                i += 1
                continue
            heapq.heappush(maxH, -needBricks)
            usedBricks += needBricks
            while ladders != 0 and usedBricks > bricks:
                t = heapq.heappop(maxH)
                t = -t
                usedBricks -= t
                ladders -= 1
            if ladders == 0 and usedBricks > bricks:
                return i
            i += 1
        return i


heights = [14,3,19,3]
#               ^
bricks = 17
ladders = 0
# maxH = [-16]
# ladders = 0
# i = 3
# needBricks = 16
# usedBricks = 16



out = Solution().furthestBuilding(heights, bricks, ladders)
print(out)


heights = [4,2,7,6,9,14,12]
bricks = 5
ladders = 1
# maxH = [-3]
# usedBricks = 3
# ladders = 0
# i = 4
# needBricks = 5

heights = [4,12,2,7,3,18,20,3,19]
bricks = 10
ladders = 2
# maxH = [-16,-5, -2]
# ladders = 0
# i = 6
# needBricks = 16
# usedBricks = 23
        