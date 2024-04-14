from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while (l <= r):
            m = l + (r - l) // 2
            neiLeft, neiRight = float('-inf'), float('-inf')
            if 0 <= m - 1 < n:
                neiLeft = nums[m-1]
            if 0 <= m + 1 < n:
                neiRight = nums[m+1]
            # isPeak
            if neiLeft < nums[m] and nums[m] > neiRight:
                return m
            if nums[m] < neiLeft:
                r = m - 1
            else:
                l = m + 1
        return -1


# edges

# 1 element
nums = [1]
#       ^
#       ^
# m = 0
# neiLeft = -inf, neiRight = -inf


# 2 element
nums = [3, 1]
#       ^
#       ^
#          ^
# m = 0
# neiLeft = -inf, neiRight = 1
out = Solution().findPeakElement(nums)
print(out)

# general
nums = [1,2,3,1]
#       ^  
#             ^
# m = 1
# neiLeft = 2, neiRight = 1
nums = [1,2,1,3,5,6,4]
#               ^
#                 ^
#                   ^
# m = 5
# neiLeft = 1, neiRight = 5

