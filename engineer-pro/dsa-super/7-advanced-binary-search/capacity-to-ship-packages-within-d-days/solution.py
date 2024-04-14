from typing import List


class Solution:
    def numShipDays(self, weights: List[int], cap: int) -> int:
        days = 0
        sumWeight = 0
        for weight in weights:
            if sumWeight + weight > cap:
                days += 1
                sumWeight = 0
            sumWeight += weight
        return days + 1

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        ans = r
        while (l <= r):
            m = l + (r - l) // 2
            if self.numShipDays(weights, m) > days:
                l = m + 1
            else:
                ans = m
                r = m - 1
        return ans
        # Time: O(n*log(sum(weights))), n is length of weights

weights = [1,2,3,4,5,6,7,8,9,10]
#                            ^
# sumWeight = 10
# days = 4
days = 5
# l = 15, r = 14
# m = 15
# ans = 15

weights = [3,2,2,4,1,4]
days = 3

weights = [1,2,3,1,1]
days = 4



# edges
# one element
weights = [100]
days = 1


# using less than days
weights = [10, 10, 20]
days = 3
out = Solution().shipWithinDays(weights, days)
print(out)


            