from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.recur(n, 0, 0, "", res)
        return res

    def recur(self, n, used_open, used_close, comb, res):
        if used_close == n:
            res.append(comb)
            return
        if used_open == n:
            self.recur(n, used_open, used_close+1, comb + ")", res)
            return
        self.recur(n, used_open+1, used_close, comb + "(", res)
        if used_open > used_close:
            self.recur(n, used_open, used_close+1, comb + ")", res)


n = 3
result = Solution().generateParenthesis(n)
print(result)
