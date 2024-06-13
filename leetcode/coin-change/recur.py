from typing import List


inf = float('inf')

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # [1, 3, 5, 7, 13]
        # amount = 23
        # coins to have 22 = 10
        # coins to have 20 = 9
        memo = {}
        def recur(amount: int) -> int:
            # base case
            if amount == 0:
                return 0
            if amount < 0:
                return -1
            if memo.get(amount):
                return memo[amount]
            # coins choices
            minCoins = inf
            for coin in coins:
                num = recur(amount - coin)
                if num != -1:
                    minCoins = min(minCoins, num)
            memo[amount] = -1 if minCoins == inf else minCoins + 1
            return memo[amount]
        return recur(amount)