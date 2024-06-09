from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        modDict = {}
        modSum = 0
        n = len(nums)
        cnt = 0
        for i in range(n):
            modSum += nums[i]
            modSum %= k
            if modSum == 0:
                cnt += 1
            cnt += modDict.get(modSum, 0)
            modDict[modSum] = modDict.get(modSum, 0) + 1
            
        return cnt