from typing import List


class Solution:
    def cntSubarray(self, nums: List[int], maxSum: int) -> int:
        n = len(nums)
        cnt = 0
        curSum = 0
        for i in range(n):
            if curSum + nums[i] > maxSum:
                cnt += 1
                curSum = 0
            curSum += nums[i]
        return cnt + 1

    def splitArray(self, nums: List[int], k: int) -> int:
        # binary search for max sum for a subarray
        l, r = max(nums), 10**9+3
        maxSum = 0
        while (l <= r):
            m = l + (r-l)//2
            cnt = self.cntSubarray(nums, m)
            if cnt == k:
                maxSum = m
            if cnt > k:
                l = m + 1
            else:
                r = m - 1
        # and I want the MIN of max sum that form k subarrays
        res = 0
        curSum = 0
        n = len(nums)
        for i in range(n):
            if curSum + nums[i] > maxSum:
                curSum = 0
            curSum += nums[i]
            res = max(res, curSum)
        return res
