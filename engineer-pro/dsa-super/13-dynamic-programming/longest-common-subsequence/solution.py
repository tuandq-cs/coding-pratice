class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # state = dp[i][j] is a longest common subsequence at i, j
        # final_ans = dp[m-1][n-1] with m is length of text1, n is length of text2
        # initial_states: dp[i][j] = 0 for every i, j
        # state transition: how can I get dp[i][j] from previous states
        m = len(text1)
        n = len(text2)
        # m (text1) * n (text2)
        # 1 <= m, n <= 2000
        dp = [[0 for _ in range(n)] for _ in range(m)]
        if text1[0] == text2[0]:
            dp[0][0] = 1 
        for i in range(1, n):
            if text1[0] == text2[i]:
                dp[0][i] = 1
            else:
                dp[0][i] = dp[0][i-1]
        for j in range(1, m):
            if text2[0] == text1[j]:
                dp[j][0] = 1
            else:
                dp[j][0] = dp[j-1][0]

        for j in range(1, m):
            for i in range(1, n):
                if text1[j] == text2[i]:
                    dp[j][i] = dp[j-1][i-1] + 1
                else:
                    dp[j][i] = max(dp[j-1][i], dp[j][i-1])
        return dp[m-1][n-1]
    
text1 = "bsbininm"
text2 = "jmjkbkjkv"
out = Solution().longestCommonSubsequence(text2, text1)
print(out)
