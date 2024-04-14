from typing import List


class Solution:
    def invalid(self, nums: List[int], k: int, begin: int, end: int, curSum: int) -> bool:
        return nums[end] * (end - begin + 1) - curSum > k

    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        n = len(nums)
        # init window
        begin, end = 0, 0
        ans = 0
        curSum = 0
        # expand window
        while (end < n):
            curSum += nums[end]
            # shink window length until valid
            while (self.invalid(nums, k, begin, end, curSum)):
                curSum -= nums[begin]
                begin += 1
            # valid
            ans = max(ans, end - begin + 1)
            end += 1
        return ans

nums = [1,2,4]
k = 5

nums = [1,4,8,13]
k = 5
out = Solution().maxFrequency(nums, k)
print(out)
