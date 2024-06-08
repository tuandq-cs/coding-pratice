from typing import List


class Solution:
    # Follow solution: https://leetcode.com/problems/continuous-subarray-sum/solutions/99499/java-o-n-time-o-k-space
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # edge case [6, 6], k = 6. So I put default mod = 0 for index -1
        modDict = {0: -1}
        modSum = 0
        n = len(nums)
        for i in range(n):
            modSum += nums[i]
            modSum %= k
            j = modDict.get(modSum)
            # (j,i]
            if j is not None and i - (j+1) + 1 > 1:
                return True
            if j is None:
                modDict[modSum] = i
        # Time: O(n), Space: O(k)
        return False


        