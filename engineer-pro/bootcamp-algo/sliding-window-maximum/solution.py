from collections import deque
from typing import List


class Solution:
    def push(self, nums: List[int], q: deque, i: int):
        while (len(q) > 0 and nums[q[-1]] < nums[i]):
            q.pop()
        q.append(i)

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = deque([])
        res = []
        for i in range(n):
            if i < (k-1):
                self.push(nums, q, i)
                continue
            # i >= k - 1
            # pop the elements of queue that not in window [i-(k-1) i]
            while (len(q) > 0 and q[0] < i-k+1): q.popleft()
            # append the i element
            self.push(nums, q, i) # this makes sure at least 1 element in queue
            res.append(nums[q[0]])
        return res

