from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMin, curMax = 1, 1
        res = nums[0]
        for num in nums:
            if num < 0: curMin, curMax = curMax, curMin
            if num == 0: curMin = curMax = 0
            curMin = min(curMin*num, num)
            curMax = max(curMax*num, num)
            res = max(res, curMax)
        return res

# [2,3,-2,4]
#         ^

# [-24, -8]
# res = 6
        