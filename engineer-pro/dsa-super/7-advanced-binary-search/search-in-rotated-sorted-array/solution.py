from typing import List


class Solution:
    def binarySearch(self, nums: List[int], target: int, l: int, r: int):
        while (l <= r):
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if nums[0] <= nums[n-1]:
            return self.binarySearch(nums, target, 0, n-1)
        # when nums[0] > nums[n-1] that mean I will always have at least 2 elements
        # and pivot != -1
        pivot = -1
        l, r = 0, n-1
        while (l <= r):
            m = l + (r - l) // 2
            if nums[m] >= nums[0]:
                l = m + 1
            else:
                pivot = m
                r = m - 1
        if target >= nums[0]:
            return self.binarySearch(nums, target, 0, pivot-1)
        return self.binarySearch(nums, target, pivot, n-1)
        # Time: O(log(n))
    

# general
nums = [4,5,6,7,0,1,2]
target = 0
target = 3

# edges
# rotated
nums = [3, 1]
target = 1
target = 3

# one element
nums = [1]
target = 1

# not rotated
nums = [1, 3]
target = 3
target = 1


out = Solution().search(nums, target)
print(out)
