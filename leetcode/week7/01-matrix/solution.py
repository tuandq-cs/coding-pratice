from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        q = deque([])
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j, 0))
                if mat[i][j] == 1:
                    mat[i][j] = -1
        while (len(q) != 0):
            i, j, dis = q.popleft()
            for d in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nI, nJ = i + d[0], j + d[1]
                if 0 <= nI < m and 0 <= nJ < n and mat[nI][nJ] == -1:
                    mat[nI][nJ] = dis + 1
                    q.append((nI, nJ, dis+1))
        return mat
        # Time: O(m*n), Space: O(m*n) in worst case (all cell = 0)


mat = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
out = Solution().updateMatrix(mat)
print(out)

mat = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 1, 1]
]
out = Solution().updateMatrix(mat)
print(out)
