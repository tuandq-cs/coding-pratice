from typing import List


inf = float('inf')

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [0 for _ in range(amount+1)]
        def recur(amount: int) -> int:
            if amount < 0:
                return -1
            if amount == 0:
                return 0
            if memo[amount] != 0:
                return memo[amount] 
            m = inf
            for coin in coins:
                numCoin = recur(amount - coin)
                if numCoin != -1:
                    m = min(m, numCoin + 1)
            memo[amount] = -1 if m == inf else m
            return memo[amount]
        return recur(amount)
        # Time: O(m*n), m: range amount, n: len of coins
        # Space: O(m)
            