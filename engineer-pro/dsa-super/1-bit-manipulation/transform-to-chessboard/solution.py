from typing import List

# This one helps me understand this problem: https://leetcode.com/problems/transform-to-chessboard/solutions/132113/java-clear-code-with-detailed-explanations/comments/433954/


class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)
        for i in range(1, n):
            for j in range(1, n):
                if board[0][0] ^ board[i][0] ^ board[0][j] ^ board[i][j] != 0:
                    return -1

        colSum = 0
        rowSum = 0
        colDiff = 0
        rowDiff = 0
        for i in range(n):
            rowSum += board[0][i]
            colSum += board[i][0]
            rowDiff += board[0][i] == (i % 2)
            colDiff += board[i][0] == (i % 2)
        if colSum != n // 2 and colSum != (n+1) // 2:
            return -1
        if rowSum != n // 2 and rowSum != (n+1) // 2:
            return -1
        if n & 1:
            # odd
            if colDiff & 1:
                colDiff = n - colDiff
            if rowDiff & 1:
                rowDiff = n - rowDiff
        else:
            # even
            colDiff = min(colDiff, n - colDiff)
            rowDiff = min(rowDiff, n - rowDiff)
        return (colDiff + rowDiff) // 2
        # Time: O(n^2)


board = [[0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1]]
out = Solution().movesToChessboard(board)
print(out)

board = [[0, 1], [1, 0]]
out = Solution().movesToChessboard(board)
print(out)

board = [[1, 0], [1, 0]]
out = Solution().movesToChessboard(board)
print(out)
