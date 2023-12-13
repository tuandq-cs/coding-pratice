from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(row: List[int], target):
            l, r = 0, len(row) - 1
            while (l <= r):
                m = l + (r - l) // 2
                if row[m] == target:
                    return m
                if row[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return -1

        for row in matrix:
            index = binary_search(row, target)
            if index != -1:
                return True
        return False


matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]
target = 5
result = Solution().searchMatrix(matrix, target)
print(result)

matrix = [
    [15],
]
target = 15
result = Solution().searchMatrix(matrix, target)
print(result)
