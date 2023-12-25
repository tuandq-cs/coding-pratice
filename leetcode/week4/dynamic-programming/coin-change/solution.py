from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        # fewest number of coins make up the amount

        def fewestNumCoins(amount: int) -> int:
            if amount < 0:
                return -1
            if amount == 0:
                return 0
            if memo.get(amount) is not None:
                return memo[amount]
            f = -1
            for coin in coins:
                tmp = fewestNumCoins(amount-coin)
                if tmp == -1:
                    continue
                if f == -1 or tmp < f:
                    f = tmp
            if f != -1:
                f += 1
            memo[amount] = f
            return f
        return fewestNumCoins(amount)


coins = [1, 2, 5]
amount = 11
out = Solution().coinChange(coins, amount)
print(out)


coins = [2]
amount = 3
out = Solution().coinChange(coins, amount)
print(out)

coins = [1]
amount = 0
out = Solution().coinChange(coins, amount)
print(out)
