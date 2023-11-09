

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 1 <= prices[i].length <= 10^5
        pointer_index = 0
        local_max_index = 0
        global_max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[pointer_index]:
                local_profit = prices[local_max_index] - prices[pointer_index]
                global_max_profit = max(local_profit, global_max_profit)
                pointer_index = i
                local_max_index = i
            else:
                if prices[i] > prices[local_max_index]:
                    local_max_index = i
                    local_profit = prices[local_max_index] - \
                        prices[pointer_index]
                    global_max_profit = max(local_profit, global_max_profit)
        return global_max_profit


# general, rise, drop random
prices = [7, 1, 5, 3, 6, 4, 1, 0, 10]
profit = Solution().maxProfit(prices=prices)
print(profit)
# corner cases
# always drop
prices = [7, 6, 5, 3]
profit = Solution().maxProfit(prices=prices)
print(profit)
prices = [7]
profit = Solution().maxProfit(prices=prices)
print(profit)
# always rise
prices = [1, 2, 4, 7]
profit = Solution().maxProfit(prices=prices)
print(profit)
