from typing import List


class Solution:
    # https://leetcode.com/problems/the-number-of-beautiful-subsets/solutions/3314361/python-house-robber-o-n
    def helper(self, counter: dict, k: int) -> int:
        # dp0 is ways without num
        # dp1 is ways with num
        prev, dp0, dp1 = 0, 1, 0
        for num in sorted(counter.keys()):
            v = 2**counter[num]
            if prev + k == num:
                dp0, dp1 = dp0 + dp1, dp0*(v-1)
            else:
                dp0, dp1 = dp0 + dp1, (dp0+dp1)*(v-1)
            prev = num
        return dp0 + dp1

    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        n = len(nums)
        counter = [{} for _ in range(k)]
        for num in nums:
            counter[num%k][num] = counter[num%k].get(num, 0) + 1
        res = 1
        for i in range(k):
            total = self.helper(counter[i], k)
            res *= total
        return res - 1


        