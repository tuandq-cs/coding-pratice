from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        minNum = nums[0]
        l, r = 0, len(nums) - 1
        while (l <= r):
            mid = l + (r - l) // 2
            if nums[0] <= nums[mid]:
                l = mid + 1
            else:
                # Rotation signal
                minNum = nums[mid]
                r = mid - 1
        return minNum


nums = [3, 4, 5, 1, 2]
result = Solution().findMin(nums)
print(result)

nums = [4, 5, 6, 7, 0, 1, 2]
result = Solution().findMin(nums)
print(result)

# Corner cases
# The rotated array is the same as the original array
nums = [11, 13, 15, 17]
# minNum = 11
# l = 4, r = 3, mid = 3
result = Solution().findMin(nums)
print(result)

nums = [3]
# minNum = 3
# l = 0, r = -1, mid = 0
result = Solution().findMin(nums)
print(result)

nums = [2, 1]
# minNum = 2
# l = 1, r = 1, mid = 0
result = Solution().findMin(nums)
print(result)
