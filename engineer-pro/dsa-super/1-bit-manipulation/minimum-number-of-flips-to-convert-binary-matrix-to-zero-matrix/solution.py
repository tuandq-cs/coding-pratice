import math
from typing import List


class Solution:
    def check(self, mask: int, mat: List[List[int]]) -> bool:
        m, n = len(mat), len(mat[0])
        cMat = [[mat[i][j] for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if testBit(i*n+j, mask):
                    self.flip(i, j, cMat)
        for i in range(m):
            for j in range(n):
                if cMat[i][j]:
                    return False
        return True

    def flip(self, i: int, j: int, mat: List[List[int]]):
        m, n = len(mat), len(mat[0])
        mat[i][j] ^= 1
        for d in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nI = i + d[0]
            nJ = j + d[1]
            if (0 <= nI < m and 0 <= nJ < n):
                mat[nI][nJ] ^= 1


    def minFlips(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        res = m*n+1
        for mask in range(1<<(m*n)):
            if mask.bit_count() >= res: continue
            if self.check(mask, mat):
                res = mask.bit_count()
        if res == m*n+1:
            return -1
        return res

def testBit(shift: int, mask: int) -> bool:
    return (1 & (mask >> shift)) == 1

mat = [[0,0],[0,1]]
out = Solution().minFlips(mat)
print(out)
