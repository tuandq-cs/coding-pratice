from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mNum = max(nums)
        n = len(nums)
        # 1 <= nums.length <= 10^5
        # 1 <= k <= 10^5
        # init window
        begin = 0
        end = -1
        cnt = 0
        ans = 0
        # expand the window when cnt < k
        while (end + 1 < n):
            end += 1
            if nums[end] == mNum:
                cnt += 1
            # shink the window when cnt == k
            while (begin <= end and cnt == k):
                if nums[begin] == mNum:
                    cnt -= 1
                ans += (n - end)
                begin += 1
        return ans