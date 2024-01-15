from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        m = {}
        for _, word in enumerate(wordDict):
            m[word] = True
        memo = {}
        def solve(s: str):
            if m.get(s) is not None:
                return True
            if memo.get(s) is not None:
                return False
            for i in range(len(s)-1):
                if m.get(s[:i+1]) is not None and solve(s[i+1:]):
                    return True
            memo[s] = False
            return False
        # Time: O(n^2 + m)
        # Space: O(m)
        # n is length of s
        # m is length of wordDict
        return solve(s)
s = "leetcode"
wordDict = ["leet","code"]
out = Solution().wordBreak(s, wordDict)
print(out)

s = "applepenapple"
wordDict = ["apple","pen"]
out = Solution().wordBreak(s, wordDict)
print(out)

s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
out = Solution().wordBreak(s, wordDict)
print(out)

s = "c"
wordDict = ["cats","dog","sand","and","cat"]
out = Solution().wordBreak(s, wordDict)
print(out)