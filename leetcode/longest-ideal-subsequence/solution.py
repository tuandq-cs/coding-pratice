class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0 for i in range(26)]
        for c in s:
            i = ord(c) - ord('a')
            l, r = max(i-k, 0), min(26, i+k+1)
            dp[i] = max(dp[l:r]) + 1
        return max(dp)