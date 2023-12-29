from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [0] * len(nums)

        def solve(i: int):
            if i == len(nums) - 1:
                return 1
            if memo[i] != 0:
                return memo[i]
            m = 1
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    m = max(solve(j)+1, m)
            memo[i] = m
            return m
        maxLength = 0
        for i in range(len(nums)):
            l = solve(i)
            if l > maxLength:
                maxLength = l
        return maxLength


nums = [10, 9, 2, 5, 3, 7, 101, 18]
out = Solution().lengthOfLIS(nums)
print(out)

nums = [0, 1, 0, 3, 2, 3]
out = Solution().lengthOfLIS(nums)
print(out)

nums = [7, 7, 7, 7, 7, 7, 7]
out = Solution().lengthOfLIS(nums)
print(out)
