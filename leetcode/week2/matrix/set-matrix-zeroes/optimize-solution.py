from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # Mark whether the first row, first col has zeroes
        firstRowHasZeroes = False
        firstColHasZeroes = False
        for i in range(len(matrix[0])):
            if matrix[0][i] == 0:
                firstRowHasZeroes = True
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                firstColHasZeroes = True

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Fill the first row, first col
        if firstColHasZeroes is True:
            for i in range(len(matrix)):
                matrix[i][0] = 0

        if firstRowHasZeroes is True:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0


matrix = [
    [0, 1, 2, 0],
    [3, 4, 5, 2],
    [1, 3, 1, 5]
]
Solution().setZeroes(matrix)
print(matrix)

matrix = [
    [0, 0, 2, 0],
    [0, 0, 5, 2],
    [1, 3, 1, 5]
]
Solution().setZeroes(matrix)
print(matrix)

matrix = [
    [6, 7, 2, 0],
    [3, 0, 5, 2],
    [1, 3, 1, 5]
]
Solution().setZeroes(matrix)
print(matrix)
