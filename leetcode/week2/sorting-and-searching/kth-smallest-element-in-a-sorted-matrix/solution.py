from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])

        def countItemsLE(v: int):
            cnt = 0
            for row in matrix:
                l, r = 0, n-1
                smallest_index = n
                while (l <= r):
                    mid = l + (r - l) // 2
                    if row[mid] > v:
                        smallest_index = mid
                        r = mid - 1
                    else:
                        l = mid + 1
                cnt += smallest_index
            return cnt

        l, h = matrix[0][0], matrix[m-1][n-1]
        k_value = -1
        while (l <= h):  # log(h - l)
            m = l + (h - l) // 2
            cnt = countItemsLE(m)  # m*log(n) or n*log(m)
            if cnt >= k:
                k_value = m
                h = m - 1
            else:
                l = m + 1
        return k_value


matrix = [
    [1, 5, 9],
    [10, 11, 13],
    [12, 13, 15]
]
target = 8
result = Solution().kthSmallest(matrix, target)
print(result)

matrix = [
    [5],
]
target = 1
result = Solution().kthSmallest(matrix, target)
print(result)
