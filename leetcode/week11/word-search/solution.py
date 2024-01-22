from collections import Counter
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Constraints:
        # 1 <= m, n <= 6, m is board.length, n is board[0].length
        # 1 <= word.length <= 15

        # inp: mxn board, a word
        # out: word exist in board? -> boolean
        m, n = len(board), len(board[0])

        def solve(i: int, j: int, wIndex: int):
            if not (0 <= i < m and 0 <= j < n and wIndex < len(word)):
                return False
            if board[i][j] != word[wIndex]:
                return False
            if wIndex == len(word) - 1:
                return True

            tmp = board[i][j]
            board[i][j] = '#'
            for d in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nI, nJ = i + d[0], j + d[1]
                if solve(nI, nJ, wIndex+1):
                    return True
            board[i][j] = tmp
            # Time + Space: O(m*n*4^len(word))
            return False

        for i in range(m):
            for j in range(n):
                if solve(i, j, 0):
                    return True
        return False


board = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"]]
word = "ABCCED"
out = Solution().exist(board, word)
print(out)

board = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"]]
word = "SEE"
out = Solution().exist(board, word)
print(out)

board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCB"
out = Solution().exist(board, word)
print(out)

board = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"]
]
word = "CCEEE"
out = Solution().exist(board, word)
print(out)

# Failed test cases

board = [
    ["A", "B", "C", "E"],
    ["S", "F", "E", "S"],
    ["A", "D", "E", "E"]
]
word = "ABCESEEEFS"
out = Solution().exist(board, word)
print(out)

board = [
    ["A", "B", "C", "E"],
    ["S", "F", "E", "S"],
    ["A", "D", "E", "E"]
]
word = "ABCEFSADEESE"
out = Solution().exist(board, word)
print(out)
