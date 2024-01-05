from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        sourceColor = image[sr][sc]
        m, n = len(image), len(image[0])
        def spread(r, c):
            image[r][c] = '#'
            for dir in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nR, nC = r + dir[0], c + dir[1]
                if (0 <= nR < m) and (0 <= nC < n) and image[nR][nC] == sourceColor:
                    spread(r + dir[0], c + dir[1])
            

        spread(sr, sc)
        for i in range(m):
            for j in range(n):
                if image[i][j] == '#':
                    image[i][j] = color
        return image
    
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2
out = Solution().floodFill(image, sr, sc, color)
print(out)