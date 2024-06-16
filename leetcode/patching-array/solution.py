from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        upTo = 1
        i = 0
        patches = 0
        while (upTo <= n):
            if i < len(nums) and nums[i] <= upTo:
                # use nums[i]
                upTo += nums[i]
                i += 1
            else:
                upTo *= 2
                patches += 1
        return patches
