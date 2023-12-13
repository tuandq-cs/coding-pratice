from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 1 <= m, n <= 200
        rows = [False for _ in range(len(matrix))]  # [False] * n
        cols = [False for _ in range(len(matrix[0]))]  # [False] * m
        # Space complexity: O(n + m)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if rows[i] is True:
                    matrix[i][j] = 0
                if cols[j] is True:
                    matrix[i][j] = 0
        # Time complexity: O(n*m), because have to loop all cells


matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
Solution().setZeroes(matrix)
print(matrix)

matrix = [
    [0, 0, 2, 0],
    [0, 0, 5, 2],
    [1, 3, 1, 5]
]
Solution().setZeroes(matrix)
print(matrix)
