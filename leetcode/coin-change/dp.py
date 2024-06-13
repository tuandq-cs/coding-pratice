from typing import List


inf = float('inf')

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # [1, 3, 5, 7, 13]
        # amount = 23
        dp = [inf] * (amount+1)
        dp[0] = 0
        for am in range(amount+1):
            # has coins choices
            for c in coins:
                if am - c < 0:
                    continue
                dp[am] = min(dp[am], dp[am-c]+1)
        return dp[am] if dp[am] != inf else -1
            
        

        