from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        # init board
        board = [['.' for _ in range(n)] for _ in range(n)]
        self.bt(0, board, ans)
        return ans

    def bt(self, row: int, board: List[List[str]], ans: List[List[str]]):
        n = len(board)
        if row == n:
            # process board
            # append to ans
            ans.append([''.join(board[row]) for row in range(n)])
            return
        # n choices in the row
        for col in range(n):
            # check if the cell is valid
            if self.isValid(row, col, board):
                # update state
                board[row][col] = 'Q'
                self.bt(row+1, board, ans)

                # remove state to choose another state
                board[row][col] = '.'
        return
    
    def isValid(self, row: int, col: int, board: List[List[str]]) -> bool:
        n = len(board)
        # check in the same col
        for i in range(row-1, -1, -1):
            if board[i][col] == 'Q': return False
        # check the left top diagonal
        i, j = row - 1, col - 1
        while (i >= 0 and j >= 0):
            if board[i][j] == 'Q': return False
            i -= 1
            j -= 1
        # check the right top diagonal
        i, j = row - 1, col + 1
        while (i >= 0 and j < n):
            if board[i][j] == 'Q': return False
            i -= 1
            j += 1
        return True
        # Time: O(n^n) * O(n) (n choices at each state, need to go deep to choose positions for n queens)
        # O(n) is time for check isValid, can improve by using hashmap
            
out = Solution().solveNQueens(4)
print(out)
