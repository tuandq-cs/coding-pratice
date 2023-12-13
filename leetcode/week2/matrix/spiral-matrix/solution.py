from typing import List

left = "L"
right = "R"
down = "D"
up = "U"


class Wall:
    def __init__(self, m, n) -> None:
        self.mostTopIndex = 0
        self.mostBottomIndex = m - 1
        self.mostLeftIndex = 0
        self.mostRightIndex = n - 1

    def hitMostRight(self, col):
        return col == self.mostRightIndex

    def hitMostLeft(self, col):
        return col == self.mostLeftIndex

    def hitMostTop(self, row):
        return row == self.mostTopIndex

    def hitMostBottom(self, row):
        return row == self.mostBottomIndex

    def getDirection(self, row, col, prevDirection):
        if prevDirection is right and self.hitMostRight(col):
            self.mostTopIndex += 1
            return down if not self.hitMostBottom(row) else None
        if prevDirection is down and self.hitMostBottom(row):
            self.mostRightIndex -= 1
            return left if not self.hitMostLeft(col) else None
        if prevDirection is left and self.hitMostLeft(col):
            self.mostBottomIndex -= 1
            return up if not self.hitMostTop(row) else None
        if prevDirection is up and self.hitMostTop(row):
            self.mostLeftIndex += 1
            return right if not self.hitMostRight(col) else None
        return prevDirection


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Time Complexity: O(m*n)
        m, n = len(matrix), len(matrix[0])
        out = []
        # Space Complexity: O(m*n) because have to save output
        wall = Wall(m, n)

        def solve(row, col, prevDirection):
            out.append(matrix[row][col])
            direction = wall.getDirection(row, col, prevDirection)
            if direction is None:
                return
            # Move to that direction
            if direction is right:
                solve(row, col+1, direction)
            elif direction is left:
                solve(row, col-1, direction)
            elif direction is up:
                solve(row-1, col, direction)
            else:
                solve(row+1, col, direction)
        solve(0, 0, right)
        return out


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# out = [1, 2, 3, 6, 9, 8, 7, 4, 5]
# row = 1
# col = 1
# prevDirection = right
# self.mostTopIndex = 2
# self.mostBottomIndex = 1
# self.mostLeftIndex = 1
# self.mostRightIndex = 1
result = Solution().spiralOrder(matrix)
print(result)

matrix = [
    [1]
]
result = Solution().spiralOrder(matrix)
print(result)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
result = Solution().spiralOrder(matrix)
print(result)
