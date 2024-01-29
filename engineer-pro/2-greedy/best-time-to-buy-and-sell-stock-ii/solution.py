from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prevPrice = prices[0]
        ans = 0
        for _, p in enumerate(prices):
            if p > prevPrice:
                ans += p - prevPrice
            prevPrice = p
        return ans


prices = [7, 1, 5, 3, 6, 4]
out = Solution().maxProfit(prices)
print(out)

prices = [1, 2, 3, 4, 5]
out = Solution().maxProfit(prices)
print(out)

prices = [7, 6, 4, 3, 1]
out = Solution().maxProfit(prices)
print(out)
