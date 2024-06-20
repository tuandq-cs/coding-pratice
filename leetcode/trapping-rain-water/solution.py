from typing import List


# https://www.youtube.com/watch?v=ZI2z5pq0TqA
class Solution:
    def trap(self, height: List[int]) -> int:
        maxL, maxR = 0, len(height) - 1
        l, r = maxL, maxR
        water = 0
        while (l <= r):
            # move l
            if height[maxL] < height[maxR]:
                add = min(height[maxL], height[maxR]) - height[l] # could neg
                water += max(0, add)
                if height[l] > height[maxL]:
                    maxL = l
                l += 1
            else: # move r
                add = min(height[maxL], height[maxR]) - height[r]
                water += max(0, add)
                if height[r] > height[maxR]:
                    maxR = r
                r -= 1
        return water
        