from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        mArea = -1
        while (l < r):
            if height[l] < height[r]:
                area = height[l] * (r - l)
                if area > mArea:
                    mArea = area
                l += 1
            else:
                area = height[r] * (r - l)
                if area > mArea:
                    mArea = area
                r -= 1
        return mArea

        # Time: O(n), Space: O(1)


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
out = Solution().maxArea(height)
print(out)

height = [1, 1]
out = Solution().maxArea(height)
print(out)
