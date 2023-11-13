from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        global_max_prod = nums[0]
        current_max_positive_prod = current_min_negative_prod = None
        for num in nums:
            if num == 0:
                current_max_positive_prod = current_min_negative_prod = None
                global_max_prod = max(
                    global_max_prod, 0)
                continue
            if num > 0:
                current_max_positive_prod = num if current_max_positive_prod is None else num * \
                    current_max_positive_prod
                current_min_negative_prod = num * \
                    current_min_negative_prod if current_min_negative_prod is not None else None
            else:
                if current_min_negative_prod is None:
                    current_min_negative_prod = num * \
                        current_max_positive_prod if current_max_positive_prod is not None else num
                    current_max_positive_prod = None
                else:
                    prev_max_pos_prod = current_max_positive_prod
                    current_max_positive_prod = current_min_negative_prod * num
                    current_min_negative_prod = prev_max_pos_prod * \
                        num if prev_max_pos_prod is not None else num
            if current_max_positive_prod is not None:
                global_max_prod = max(
                    global_max_prod, current_max_positive_prod)
        return global_max_prod
# Given
# M1: sub array with max positive prod
# M2: sub array with min negative prod


# General cases
# 1. num < 0, M1 not empty, M2 is empty
nums = [2, 3, -1, 9]
# Expected prod of [9]: 9
# global_max_prod = 9
# current_max_positive_prod = 9
# current_min_negative_prod = -36
result = Solution().maxProduct(nums=nums)
print(result)
# 2. num < 0, M1 not empty, M2 not empty
nums = [2, 2, -1, 3, -2, -6]
# Expected prod of [3, -2, -6]: 36

# global_max_prod = 36
# current_max_positive_prod = 36
# current_min_negative_prod = -48
result = Solution().maxProduct(nums=nums)
print(result)

# 3. num = 0 in the middle
nums = [2, -1, 0, -3, -1, 0, -2, 5]
# Expected prod of [5]: 5

# global_max_prod = 5
# current_max_positive_prod = 5
# current_min_negative_prod = -10
result = Solution().maxProduct(nums=nums)
print(result)
# Corner cases
# 1 item
nums = [-2]
# global_max_prod = -2
# current_max_positive_prod = None
# current_min_negative_prod = -2
result = Solution().maxProduct(nums=nums)
print(result)

nums = [-2, 0, -1]
# global_max_prod = -2
# current_max_positive_prod = None
# current_min_negative_prod = None
result = Solution().maxProduct(nums=nums)
print(result)
