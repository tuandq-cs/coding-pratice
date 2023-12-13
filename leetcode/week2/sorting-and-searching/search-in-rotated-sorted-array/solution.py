from typing import List

# My solution is hard to understand

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         def recur(l: int, r: int):
#             if l > r:
#                 return -1
#             m = l + (r - l) // 2
#             if nums[m] == target:
#                 return m
#             if nums[l] == target:
#                 return l
#             if nums[r] == target:
#                 return r

#             if nums[m] < target:
#                 if nums[m] < nums[r] and nums[r] < target:
#                     return recur(l, m - 1)
#                 return recur(m+1, r)
#             else:  # l  t  m    r
#                 if nums[l] < nums[m] and nums[l] > target:
#                     return recur(m+1, r)
#                 return recur(l, m-1)
#         return recur(0, len(nums)-1)


# This one I found is easy to understand
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Check if left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Otherwise, right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
result = Solution().search(nums, target)
print(result)

nums = [4, 5, 6, 7, 0, 1, 2]
target = 3
result = Solution().search(nums, target)
print(result)

nums = [1]
target = 0
result = Solution().search(nums, target)
print(result)

nums = [4, 5, 6, 7, 8, 1, 2, 3]
target = 8
result = Solution().search(nums, target)
print(result)

nums = [5, 1, 2, 3, 4]
target = 1
result = Solution().search(nums, target)
print(result)
