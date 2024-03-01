from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        begin, end =  0, 0
        ans = n + 1
        s = 0
        # expand the window
        while (end < n):
            s += nums[end]
            # shink the window if sum >= target
            while (begin <= end and s >= target):
                # [begin, end]
                ans = min(ans, end - begin + 1)
                s -= nums[begin]
                begin += 1
            # sum < target
            end += 1
        return ans if ans != n + 1 else 0
            