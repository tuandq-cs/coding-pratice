from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}
        for i, num in enumerate(nums):
            if memo.get(target-num) is not None:
                return [memo[target-num], i]
            memo[num] = i

nums = [2,7,11,15]
target = 9
out = Solution().twoSum(nums, target)
print(out)
