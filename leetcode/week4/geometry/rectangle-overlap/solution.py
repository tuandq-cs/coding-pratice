from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # x1, y1, x2, y2
        return (
            (rec1[0] < rec2[2] and rec2[0] < rec1[2]) or
            (rec2[0] < rec1[2] and rec1[0] < rec2[2])
        ) and (
            (rec1[1] < rec2[3] and rec2[1] < rec1[3]) or
            (rec2[1] < rec1[3] and rec1[1] < rec2[3])
        )
            
rec1 = [0,0,2,2]
rec2 = [1,1,3,3]
print(Solution().isRectangleOverlap(rec1, rec2))

rec1 = [0,0,1,1]
rec2 = [1,0,2,1]
print(Solution().isRectangleOverlap(rec1, rec2))

rec1 = [0,0,1,1]
rec2 = [2,2,3,3]
print(Solution().isRectangleOverlap(rec1, rec2))
