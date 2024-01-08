from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        for num in nums:
            if counter.get(num) is None:
                counter[num] = 0
            counter[num] += 1
            if counter[num] > (len(nums) // 2):
                return num
        # Overall complexity: O(n) in time & O(n) in space

        # There is an optimal solution: using Moore's Voting Algorithm, take O(n) in time and O(1) in space


nums = [3, 2, 3]
out = Solution().majorityElement(nums)
print(out)

nums = [2, 2, 1, 1, 1, 2, 2]
out = Solution().majorityElement(nums)
print(out)
