from collections import deque
from typing import List

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m = len(land)
        n = len(land[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]
        def isValid(i: int, j: int):
            return (0 <= i < m and 0 <= j < n and land[i][j] == 1 and not visited[i][j])

        def bfs(i: int, j: int):
            far = (i, j)
            q = deque([])
            q.append((i, j))
            while len(q) > 0:
                x, y = q.pop()
                valid = isValid(x, y)
                visited[x][y] = 1
                if not valid:
                    continue
                far = (max(far[0], x), max(far[1], y))
                for d in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    nX, nY = x + d[0], y + d[1]
                    if isValid(nX, nY):
                        q.append((nX, nY))
            return [i, j, far[0], far[1]]
        res = []
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and land[i][j] == 1:
                    res.append(bfs(i, j))
        return res