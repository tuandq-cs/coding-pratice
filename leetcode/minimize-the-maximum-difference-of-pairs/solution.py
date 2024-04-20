from typing import List


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        # ensure no index appears more than once amongst the p pairs.
        # goal: got p pairs, their diff is smallest between all pairs
        def countPairs(diff: int) -> int:
            i = 1
            ans = 0
            while (i < n):
                if nums[i] - nums[i-1] <= diff:
                    i += 2
                    ans += 1
                else:
                    i += 1
            return ans

        if p == 0:
            return 0
        nums = sorted(nums)
        n = len(nums)
        l, r = 0, nums[n-1] - nums[0]
        res = r
        while (l <= r):
            m = l + (r-l)//2
            if countPairs(m) < p:
                l = m + 1
            else:
                res = m
                r = m - 1
        return res
        # Time: O(n*log(max(nums))) + O(n*log(n))

        
            
        

# [3,4,2,3,2,1,2], p = 3
# [1, 2, 2, 2, 3, 3, 4]
# [0, 3]
# diff = 0
#  ^
# pq = []
# diff = 

# nums = [4,2,1,2], p = 1
# [1, 2, 2, 4]
#        ^
# diff = 2
# pg = [0]

# [10,1,2,7,1,3], p = 2
# [1, 1, 2, 3, 7, 10]
#              ^
# pg = [1, 0]
# diff = 1

