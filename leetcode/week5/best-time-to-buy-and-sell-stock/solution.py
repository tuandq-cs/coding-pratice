from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        gProfit = 0
        mIndex = 0
        for i, price in enumerate(prices):
            if (price - prices[mIndex]) < 0:
                mIndex = i
                continue
            if (price - prices[mIndex]) > gProfit:
                gProfit = price - prices[mIndex]
        return gProfit
    
prices = [7,1,5,3,6,4]
out = Solution().maxProfit(prices)
print(out)

prices = [7,6,4,3,1]
out = Solution().maxProfit(prices)
print(out)

prices = [7]
out = Solution().maxProfit(prices)
print(out)