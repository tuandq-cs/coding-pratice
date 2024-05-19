from typing import List


class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        cnt = 0
        s = 0
        for i in range(n):
            if nums[i]^k > nums[i]:
                cnt += 1
                s += nums[i]^k
            else:
                s += nums[i]
        if cnt % 2:
            minDiff = -1
            for i in range(n):
                diff = abs((nums[i]^k)-nums[i])
                if minDiff == -1 or diff < minDiff:
                    minDiff = diff
            s -= minDiff
        return s
            
        
