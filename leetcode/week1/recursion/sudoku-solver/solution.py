from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.row_map = [{} for _ in range(9)]
        self.col_map = [{} for _ in range(9)]
        self.sub_box_map = [{} for _ in range(9)]
        self.board = board
        for r in range(9):
            for c in range(9):
                if self.board[r][c] != ".":

                    self.mark_choice(self.board[r][c], r, c)
        self.recur(0, 0)
        print(self.board)

    def compute_sub_box_index(self, r: int, c: int):
        return r // 3 * 3 + c // 3

    def is_valid_choice(self, choice: str, r: int, c: int):
        sub_box_index = self.compute_sub_box_index(r, c)
        return self.row_map[r].get(choice) is None and self.col_map[c].get(choice) is None and self.sub_box_map[sub_box_index].get(choice) is None

    def mark_choice(self, choice: str, r: int, c: int):
        sub_box_index = self.compute_sub_box_index(r, c)
        self.row_map[r][choice] = True
        self.col_map[c][choice] = True
        self.sub_box_map[sub_box_index][choice] = True
        self.board[r][c] = choice

    def unmark_choice(self, choice: str, r: int, c: int):
        sub_box_index = self.compute_sub_box_index(r, c)
        del self.row_map[r][choice]
        del self.col_map[c][choice]
        del self.sub_box_map[sub_box_index][choice]
        self.board[r][c] = "."

    def recur(self, r: int, c: int):
        if r > 8:
            return True
        if c > 8:
            return self.recur(r + 1, 0)
        if self.board[r][c] != ".":
            return self.recur(r, c+1)

        for num in range(1, 10):  # choices: 1-9
            choice = str(num)
            if self.is_valid_choice(choice, r, c):
                self.mark_choice(choice, r, c)
                if self.recur(r, c+1):
                    return True
                self.unmark_choice(choice, r, c)
        return False


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
Solution().solveSudoku(board)
