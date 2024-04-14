from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0]
        pivot = nums[len(nums)//2]
        leftNums = [x for x in nums if x > pivot]
        pivotNums = [x for x in nums if x == pivot]
        rightNums = [x for x in nums if x < pivot]
        if (k <= len(leftNums)):
            return self.findKthLargest(leftNums, k)
        k -= len(leftNums)
        if (k <= len(pivotNums)):
            return pivot
        k -= len(pivotNums)
        return self.findKthLargest(rightNums, k)
    
nums = [3,2,1,5,6,4]
k = 2
out = Solution().findKthLargest(nums, k)
print(out)

nums = [3,2,3,1,2,4,5,5,6]
k = 4
out = Solution().findKthLargest(nums, k)
print(out)