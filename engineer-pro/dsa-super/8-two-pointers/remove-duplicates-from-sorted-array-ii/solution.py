from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = j = 0
        while(i < len(nums)):
            # i <= j
            if j >= 2 and nums[i] == nums[j-2]:
                i += 1
                continue
            nums[j] = nums[i]
            j += 1
            i += 1
        return j

nums = [1,1,1,2,2,3]
#i                  ^
#j                ^

# nums = [1, 1, 2, 2, 3]

nums = [0,0,1,1,1,1,2,3,3]
out = Solution().removeDuplicates(nums)
print(out)