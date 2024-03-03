from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.bt(n, '', 0, ans)
        return ans
        
    def bt(self, n: int, cur: str, numOpen: int, ans: List[str]):
        if len(cur) == 2*n:
            ans.append(cur)
            return
        if numOpen < n:
            self.bt(n, cur + '(', numOpen+1, ans)
        
        if len(cur) - numOpen < numOpen:
            self.bt(n, cur + ')', numOpen, ans)
