from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse=True)
        ans = -1
        preSum = []
        curSum = 0
        for i in range(len(nums)):
            curSum += nums[i]
            preSum.append(curSum)

        for i in range(len(nums)-2):
            # nums[i] < sum(i+1, k)
            pe = preSum[-1] - preSum[i]
            if pe > nums[i]:
                ans = max(ans, pe + nums[i])
        return ans

nums = [1,12,1,2,5,50,3]
# nums = [50, 12, 5, 3, 2, 1, 1]
#                 ^
# preSum = [50, 62, 67, 70, 72, 73, 74]
# ans = 12

nums = [5,5,5]
nums = [5,5,50]
out = Solution().largestPerimeter(nums)
print(out)