from typing import List

def searchLowerBound(nums: List[int], target: int) -> int:
    l = 0
    r = len(nums) - 1
    ans = -1
    while (l <= r):
        m = l + (r - l) // 2
        if nums[m] >= target:
            ans = m
            r = m - 1
        else:
            l = m + 1
    return ans

def searchUpperBound(nums: List[int], target: int) -> int:
    l = 0
    r = len(nums) - 1
    ans = -1
    while (l <= r):
        m = l + (r - l) // 2
        if nums[m] <= target:
            ans = m
            l = m + 1
        else:
            r = m - 1
    return ans 

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1 if lower <= nums[0] <= upper else 0
        m = len(nums) // 2
        cnt = 0
        # a = self.countRangeSum(nums[:m], lower, upper)
        # b = self.countRangeSum(nums[m:], lower, upper)
        # cnt += a + b
        cnt += self.countRangeSum(nums[:m], lower, upper)
        cnt += self.countRangeSum(nums[m:], lower, upper)
        leftNums = sorted(nums[:m])
        rightNums = sorted(nums[m:])
        # calc prefix sum
        rightPrefix = [0]*len(rightNums)
        curSum = 0
        for i, num in enumerate(rightNums):
            curSum += num
            rightPrefix[i] = curSum
        curSum = 0
        leftSum = sum(leftNums)
        for i, num in enumerate(leftNums):
            lbIndex = searchLowerBound(rightPrefix, lower + leftSum - curSum)
            if lbIndex == -1:
                continue
            ubIndex = searchUpperBound(rightPrefix, upper + leftSum - curSum)
            ubIndex = ubIndex if ubIndex != -1 else len(rightPrefix) - 1
            cnt += (ubIndex - lbIndex + 1)
            curSum += num
        return cnt
    
nums = [-2,5,-1]
out = Solution().countRangeSum(nums, -2, 2)
print(out)
