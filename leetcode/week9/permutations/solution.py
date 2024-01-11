from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[nums[0]]]
        perm = []
        for i, num in enumerate(nums):
            subNums = nums[:i]
            if i < len(nums) - 1:
                subNums.extend(nums[i+1:])
            subPerms = self.permute(subNums)
            for subPerm in subPerms:
                perm.append([num]+subPerm)
        return perm
    
nums = [1,2,3]
out = Solution().permute(nums)
print(out)

nums = [0,1]
out = Solution().permute(nums)
print(out)

nums = [1]
out = Solution().permute(nums)
print(out)