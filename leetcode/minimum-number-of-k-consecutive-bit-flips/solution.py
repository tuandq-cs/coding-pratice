from typing import List


class Solution:
    # https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/solutions/238609/java-c-python-one-pass-and-o-1-space/comments/236804
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        # [0, 1, 0, 0, 1, 1, 1, 0, 1, 0], k = 4
        n = len(nums)
        flipped = [0] * n
        numFlipsWin = 0 # total flip times at current fixed k-length window
        ans = 0
        for i in range(n):
            
            if i >= k:
                if flipped[i-k]: # remove the i-k from window
                    numFlipsWin -= 1

            if numFlipsWin % 2 == nums[i]: # need to flip at current i
                # if we still flip at i and i + k > n that mean slip useless
                if i + k > n:
                    return -1
                numFlipsWin += 1
                ans += 1
                flipped[i] = True
        return ans
                