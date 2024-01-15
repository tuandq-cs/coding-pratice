from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = [0, 0, 0]
        for num in nums:
            counter[num] += 1
        j = 0
        for i in range(len(nums)):
            while counter[j] == 0:
                j += 1
            nums[i] = j
            counter[j] -= 1
        # Time: O(n), Space: O(1) because length of counter always = 3


nums = [2, 0, 2, 1, 1, 0]
# counter = [0, 0, 0]
# j = 2
# nums = [0, 0, 1, 1, 2, 2]
Solution().sortColors(nums)
print(nums)

nums = [2, 2, 2, 2, 0, 2]
# counter = [0, 0, 3]
# j = 2
# nums = [0, 2, 2, 2, 2]
Solution().sortColors(nums)
print(nums)

nums = [2, 0, 1]
Solution().sortColors(nums)
print(nums)

nums = [2]
Solution().sortColors(nums)
print(nums)
