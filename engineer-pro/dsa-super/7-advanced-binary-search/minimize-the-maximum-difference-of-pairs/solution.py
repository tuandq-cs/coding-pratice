from typing import List


class Solution:
    def findPairs(self, nums: List[int], dif: int) -> set:
        pairs = set()
        counter = {}
        for i, num in enumerate(nums):
            # a + b = dif
            # a + b = -dif
            if counter.get(num) is None:
                counter[num] = []
            counter[num].append(i)
        for k in counter:
            

    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0
        l, r = 0, max(nums) - min(nums)
        ans = r
        while (l <= r):
            m = l + (r - l) // 2
            pairs = self.findPairs(nums, m)
            for pair in pairs:
                newNums = [nums[i] for i in len(nums) if i != pair[0] and i != pair[1]]
                if self.minimizeMax(newNums, p-1) <= p:
                    ans = p
                    r = m - 1
            if ans > p:
                l = m + 1
        return ans

nums = [10,1,2,7,1,3]
p = 2
Solution().minimizeMax(nums, p)
