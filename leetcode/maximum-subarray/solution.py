from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = max(nums) # all negative [-2, -1, -3]
        curSum = 0
        for num in nums:
            if curSum + num < 0:
                curSum = 0
            else:
                curSum += num
                res = max(res, curSum)
        return res
