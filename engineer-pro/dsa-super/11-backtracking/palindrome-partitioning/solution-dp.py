from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        memo = {}
        return self.recur(s, 0, memo)

        
    def recur(self, s: str, idx: int, memo: dict):
        if idx == len(s):
            return []
        if memo.get(idx) is not None:
            return memo[idx]
        
        allPar = []
        # n choices
        for j in range(idx, len(s)):
            # check palindrome
            if self.isValid(s, idx, j):
                # choose this path
                tmp = [s[idx:j+1]]
                lSubP = self.recur(s, j+1, memo)
                if len(lSubP) == 0:
                    allPar.append(tmp)
                for subP in lSubP:
                    allPar.append(tmp + subP)
        memo[idx] = allPar
        return memo[idx]
        # Time: O(n^2) * O(n)
        # O(n) for check valid
        # O(n^2) because each index has n choices

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
        