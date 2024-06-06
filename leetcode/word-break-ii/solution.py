from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        ans = []
        wordSet = set(wordDict)
        def recur(i: int, curS: str, words: List[str]):
            if i == n:
                if curS == "":
                    ans.append(" ".join(words))
                return
            curS += s[i]
            if curS in wordSet:
                newWords = words.copy()
                newWords.append(curS)
                recur(i+1, "", newWords)
            recur(i+1, curS, words)
        recur(0, "", [])
        # Time: O(2^n), n = 20 (length of s)
        return ans
