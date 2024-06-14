from typing import List


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        # [3,2,1,2,1,7]
        # {1: 2, 2: 2, 3: 1, 7: 1}
        # {1: 1, 2: 3, 3: 1, 7: 1} +1 move
        # {1: 1, 2: 1, 3: 3, 7: 1} +2 move
        # {1: 1, 2: 1, 3: 1, 4: 2, 7: 1} +2 move
        # {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 7: 1} + 1move
        n = len(nums)
        nm = max(nums) + n + 3
        count = [0] * nm
        for num in nums: # O(n)
            count[num] += 1
        moves = 0
        for num in range(nm-1): # O(m)
            if count[num] <= 1:
                continue
            move = count[num] - 1
            count[num+1] += move
            moves += move
        # Time: O(n+m), n is length of nums, m is max of nums[i], 0 <= nums[i] <= 10^5
        return moves

# edge case
# nums = [10**5] * 10**5
# out = Solution().minIncrementForUnique(nums)
# print(out)