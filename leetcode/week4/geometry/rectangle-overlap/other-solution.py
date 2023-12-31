from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # x1, y1, x2, y2
        l1, b1, r1, t1 = rec1
        l2, b2, r2, t2 = rec2
        width = min(r1, r2) - max(l1, l2)
        height = min(t1, t2) - max(b1, b2)
        return width > 0 and height > 0

            
rec1 = [0,0,2,2]
rec2 = [1,1,3,3]
print(Solution().isRectangleOverlap(rec1, rec2))

rec1 = [0,0,1,1]
rec2 = [1,0,2,1]
print(Solution().isRectangleOverlap(rec1, rec2))

rec1 = [0,0,1,1]
rec2 = [2,2,3,3]
print(Solution().isRectangleOverlap(rec1, rec2))
