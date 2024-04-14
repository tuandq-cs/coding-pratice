from typing import List


class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        m = {} # Only has numbers from 0 -> 2^16
        for i in range(len(nums)): # O(n^2)
            for j in range(len(nums)):
                v = nums[i] & nums[j]
                if m.get(v) is None:
                    m[v] = 0
                m[v] +=1
        cnt = 0
        for k in range(len(nums)): # O(n)
            for v in m: # O(2^16) ~ O(1)
                if v & nums[k] == 0:
                    cnt += m[v]
        # Time: O(n^2), Space: O(1), m only has 2^16 = 18 items
        return cnt

nums = [2,1,3]
out = Solution().countTriplets(nums)
print(out)

nums = [0,0,0]
out = Solution().countTriplets(nums)
print(out)