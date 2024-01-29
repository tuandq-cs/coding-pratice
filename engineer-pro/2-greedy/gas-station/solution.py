from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        profit = [None]*n
        for i in range(0, n-1):
            profit[i] = gas[i+1] - cost[i]
        profit[n-1] = gas[0] - cost[n-1]
        if sum(profit) < 0:
            return -1
        mIndex = None
        for i in range(n):
            if (gas[i]-cost[i] >= 0):
                if mIndex is None or profit[i] + gas[i] > profit[mIndex] + gas[mIndex]:
                    mIndex = i
        return mIndex


gas = [5, 5, 1, 3, 4]
cost = [8, 1, 7, 1, 1]
out = Solution().canCompleteCircuit(gas, cost)
print(out)

gas = [5, 8, 2, 8]
cost = [6, 5, 6, 6]
out = Solution().canCompleteCircuit(gas, cost)
print(out)

gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
out = Solution().canCompleteCircuit(gas, cost)
print(out)

gas = [2, 3, 4]
cost = [3, 4, 3]
out = Solution().canCompleteCircuit(gas, cost)
print(out)
