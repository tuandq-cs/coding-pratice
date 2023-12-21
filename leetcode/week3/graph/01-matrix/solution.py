from typing import List


# Not working, please keep doing this

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        distMat = [[None for _ in range(n)] for _ in range(m)]
        calculating = {}

        def calcDist(r: int, c: int):
            if distMat[r][c] != None:
                return distMat[r][c]
            if mat[r][c] == 0:
                distMat[r][c] = 0
                return 0
            calculating[f'{r}{c}'] = True
            nearestDist = 10**10
            for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nextR = r + direction[0]
                nextC = c + direction[1]
                if (0 <= nextR < m and 0 <= nextC < n and not calculating.get(f'{nextR}{nextC}')):
                    neighborDist = calcDist(nextR, nextC)
                    nearestDist = min(neighborDist + 1, nearestDist)
            distMat[r][c] = nearestDist
            del calculating[f'{r}{c}']
            return nearestDist
        for i in range(m):
            for j in range(n):
                calcDist(i, j)
        return distMat


mat = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
result = Solution().updateMatrix(mat)
print(result)

mat = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 1, 1]
]
result = Solution().updateMatrix(mat)
print(result)
