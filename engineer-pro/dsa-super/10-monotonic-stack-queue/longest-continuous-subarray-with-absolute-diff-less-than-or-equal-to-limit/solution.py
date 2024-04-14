from collections import deque
from typing import List


class Solution:
    def absDiff(self, nums, minQueue, maxQueue) -> int:
        return nums[maxQueue[0]] - nums[minQueue[0]]
    
    def insertMinQueue(self, minQueue, nums, idx: int):
        while len(minQueue) > 0 and nums[minQueue[-1]] > nums[idx]:
            minQueue.pop()
        minQueue.append(idx)

    def insertMaxQueue(self, maxQueue, nums, idx: int):
        while len(maxQueue) > 0 and nums[maxQueue[-1]] < nums[idx]:
            maxQueue.pop()
        maxQueue.append(idx)
        

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        # init window with length = 1
        begin = 0
        end = 0
        # minQueue, maxQueue
        minQueue = deque([])
        maxQueue = deque([])
        # track index of the max subarray
        res = (0, 0)
        # 1 <= nums.length <= 10^5
        # expand the window
        while (end < n):
            self.insertMinQueue(minQueue, nums, end)
            self.insertMaxQueue(maxQueue, nums, end)
            # shink the window if not sastify the condition, we don't want to shink when len queue == 1
            while (begin < end and self.absDiff(nums, minQueue, maxQueue)) > limit:
                if minQueue[0] == begin:
                    minQueue.popleft()
                if maxQueue[0] == begin:
                    maxQueue.popleft()
                begin += 1
            # sastify the condition
            if self.absDiff(nums, minQueue, maxQueue) <= limit and (end - begin) > (res[1] - res[0]):
                res = (begin, end)
            end += 1
        return (res[1] - res[0]) + 1