from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [0]*len(nums)
        def solve(i: int):
            if memo[i] != 0:
                return memo[i]
            maxLength = 1
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    maxLength = max(solve(j)+1, maxLength)
            memo[i] = maxLength
            return maxLength
        m = 1
        for i, _ in enumerate(nums):
            m = max(solve(i), m)
        return m
    
nums = [10,9,2,5,3,7,101,18]
out = Solution().lengthOfLIS(nums)
print(out)

nums = [0,1,0,3,2,3]
out = Solution().lengthOfLIS(nums)
print(out)

nums = [7,7,7,7,7,7,7]
out = Solution().lengthOfLIS(nums)
print(out)

