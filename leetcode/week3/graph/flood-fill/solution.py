from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        startingColor = image[sr][sc]
        m, n = len(image), len(image[0])

        def dfs(r: int, c: int):
            if not (0 <= r < m and 0 <= c < n) or image[r][c] != startingColor:
                return
            image[r][c] = '#'
            for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nextR = r + direction[0]
                nextC = c + direction[1]
                dfs(nextR, nextC)
        dfs(sr, sc)
        for i in range(m):
            for j in range(n):
                if image[i][j] == '#':
                    image[i][j] = color
        return image


image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1
color = 2
result = Solution().floodFill(image, sr, sc, color)
print(result)

image = [[0, 0, 0], [0, 0, 0]]
sr = 0
sc = 0
color = 0
result = Solution().floodFill(image, sr, sc, color)
print(result)
