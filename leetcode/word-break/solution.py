from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        memo = [True] * n
        def recur(i: int) -> bool:
            if i == n:
                return True
            if memo[i] == False:
                return False
            for j in range(i, n):
                if s[i:j+1] in wordSet and recur(j+1):
                    return True
            memo[i] = False
            return False
        return recur(0)