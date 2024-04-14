from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        self.recur(s, 0, [], ans)
        return ans

        
    def recur(self, s: str, idx: int, par: List[str], ans: List[List[str]]):
        if idx == len(s):
            ans.append(par.copy())
            return
        # n choices
        for j in range(idx, len(s)):
            # check palindrome
            if self.isValid(s, idx, j):
                # choose this path
                par.append(s[idx:j+1])
                self.recur(s, j+1, par, ans)

                # unchoose this path
                par.pop()

        # Time: O(n^n) * O(n)

    def isValid(self, s: str, begin: int, end: int) -> bool:
        while (begin <= end):
            if s[begin] != s[end]:
                return False
            begin += 1
            end -= 1
        return True
    
s = "aab"
#     ^^
# idx = 0
# choices [0, 2]
# j = 0, valid
#       par = ["a"]
#       idx = 1
#       choices [1, 2]
#       j = 1, valid
#           valid: par = ["a", "a"]
#               idx = 2
#               choices = [2, 2]
#               j = 2
#                   valid: par = ["a", "a", "b"]
#                       idx = 3
#                       ans = [["a", "a", "b"]]
#                   par = ["a", "a"]
#           par = ["a"]
#       j = 2, not valid:
#
s = "a"
s = "aaaabba"
out = Solution().partition(s)
print(out)
        