from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        self.recur(nums, 0, [], res)
        return res

    def recur(self, nums, start, comb, res):
        res.append(comb.copy())
        for i in range(start, len(nums)):
            comb.append(nums[i])
            self.recur(nums, i+1, comb, res)
            comb.pop()


# General case
nums = [9, 3, 8]
# Expected = [[], [3], [3, 8], [3, 8, 9], [3, 9], [8], [8, 9], [9]]
result = Solution().subsets(nums)
print(result)

# Corner case
# nums has one item
nums = [0]
# Expected = [[], [0]]
result = Solution().subsets(nums)
print(result)
