from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = f = 0
        while True:
            s = nums[s]
            f = nums[nums[f]]
            if s == f:
                break
        s2 = 0
        while s != s2:
            s2 = nums[s2]
            s = nums[s]
        return s

nums = [1,3,4,2,2]
#       ^
#       ^
# s = 0
# f = 0

nums = [3,1,3,4,2]
#               ^
#         ^
out = Solution().findDuplicate(nums)
print(out)

