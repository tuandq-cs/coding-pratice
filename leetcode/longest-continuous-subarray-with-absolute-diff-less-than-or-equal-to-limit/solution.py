from collections import deque
from typing import List


class Solution:
    def pushAsc(self, ascQ, nums, end):
        while (ascQ and nums[end] < nums[ascQ[-1]]):
            ascQ.pop()
        ascQ.append(end)

    def pushDesc(self, descQ, nums, end):
        while (descQ and nums[end] > nums[descQ[-1]]):
            descQ.pop()
        descQ.append(end)

    def pop(self, q, begin):
        while (q and q[0] <= begin):
            q.popleft()

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # init window
        begin = 0
        end = -1
        n = len(nums)
        ascQ, descQ = deque([]), deque([])
        res = 0
        # expand window
        while (end < n-1):
            end += 1
            # push to mono queue
            self.pushAsc(ascQ, nums, end)
            self.pushDesc(descQ, nums, end)
            # shrink when any queue is empty or max - min > limit
            while (begin <= end and ascQ and descQ and nums[descQ[0]] - nums[ascQ[0]] > limit):
                # pop any element out of window
                self.pop(ascQ, begin)
                self.pop(descQ, begin)
                begin += 1
            res = max(res, end-begin+1)
        return res
            