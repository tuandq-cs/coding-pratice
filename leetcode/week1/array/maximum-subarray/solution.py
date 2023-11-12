from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.maxSubArray3(nums=nums)

    def maxSubArray2(self, nums: List[int]):
        # Time complexity: O(n)
        # Space complexity: O(1)
        cum_sum = 0 + nums[0]
        result = cum_sum
        prefix_cum_sum = min(0, nums[0])
        for r in range(1, len(nums)):
            cum_sum += nums[r]
            result = max(result, cum_sum - prefix_cum_sum)
            if cum_sum < prefix_cum_sum:
                prefix_cum_sum = cum_sum
        return result

    def maxSubArray3(self, nums: List[int]):
        global_max = nums[0]
        current_max = nums[0]
        for i in range(1, len(nums)):
            current_max = max(nums[i], current_max + nums[i])
            global_max = max(global_max, current_max)
        return global_max


# General case
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = Solution().maxSubArray(nums=nums)
print(result)
nums = [5, 4, -1, 7, 8]
result = Solution().maxSubArray(nums=nums)
print(result)
# cum_sum = 23
# prefix_cum_sum = 0
# result = 23
# Corner case
# Just one item
nums = [1]
result = Solution().maxSubArray(nums=nums)
print(result)
