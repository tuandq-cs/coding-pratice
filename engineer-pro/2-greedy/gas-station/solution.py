from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        curGas = 0
        sIndex = 0
        i = 0
        remainGas = 0
        while (i < n):
            remainGas += gas[i] - cost[i]
            curGas += gas[i] - cost[i]
            if curGas < 0:
                sIndex = i+1
                curGas = 0
            i += 1
        return -1 if remainGas < 0 else sIndex


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
