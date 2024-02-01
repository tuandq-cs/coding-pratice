from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        # 1 <= nums.length <= 5 * 104
        if len(nums) < 2:
            return 0
        if len(nums) == 2:
            return 1 if nums[0] > 2*nums[1] else 0
        l = 0
        r = len(nums) - 1
        m = l + (r - l) // 2
        cnt = 0
        cnt += self.reversePairs(nums[l:m])
        cnt += self.reversePairs(nums[m:])
        # merge sort
        leftNums = self.mergeSort(nums[l:m])
        rightNums = self.mergeSort(nums[m:])
        lP = 0
        rP = 0
        while (lP < len(leftNums)):
            while (rP < len(rightNums)):
                if leftNums[lP] > 2*rightNums[rP]:
                    cnt += len(rightNums) - rP
                    break
                rP += 1
            lP += 1
        return cnt

    def mergeSort(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        l = 0
        r = len(nums) - 1
        m = l + (r - l) // 2
        leftNums = self.mergeSort(nums[l:m+1])
        rightNums = self.mergeSort(nums[m+1:])
        # merge
        lP = 0
        rP = 0
        p = 0
        while (lP < len(leftNums) and rP < len(rightNums)):
            if leftNums[lP] > rightNums[rP]:
                nums[p] = leftNums[lP]
                lP += 1
            else:
                nums[p] = rightNums[rP]
                rP += 1
            p += 1
        while (lP < len(leftNums)):
            nums[p] = leftNums[lP]
            lP += 1
            p += 1
        while (rP < len(rightNums)):
            nums[p] = rightNums[rP]
            rP += 1
            p += 1
        return nums


nums = [5, 4, 3, 2, 1]
out = Solution().reversePairs(nums)
print(out)
# m = 2
# cnt = 0
# [5, 4] +0
# [3, 2, 1] +1
# lP = 0, rP = 3, +(5-3)
# lP = 1, rP = 4, +(5-4)
# cnt = 0 + 1 + 2 + 1

nums = [1, 3, 2, 3, 1]
# m = 2
# cnt = 0
# [1, 3] cnt += 0
# [2, 3, 1] cnt += 1
# lP = 2
# rP = 5 => cnt += 5 - 4
# cnt = 0 + 1 + 5 - 4 = 2


nums = [2, 4, 3, 5, 1]
