from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # 0: is -
        # 1: is +
        ans = 0
        for bitmask in range(0, 1 << n): # O(2^n)
            if self.calcSum(bitmask, nums) == target: # O(n)
                ans += 1
        return ans
    
    def calcSum(self, bitmask: int, nums: List[int]):
        n = len(nums)
        s = 0
        for i in range(n):
            sign = getSign(bitmask)
            s += sign * nums[i]
            bitmask = bitmask >> 1
        return s
    
def getSign(bitmask: int) -> int:
    return 1 if bitmask & 1 == 1 else -1

nums = [27,22,39,22,40,32,44,45,46,8,8,21,27,8,11,29,16,15,41,0]
target = 10
out = Solution().findTargetSumWays(nums, target)
print(out)