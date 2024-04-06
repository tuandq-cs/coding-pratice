from collections import deque
from typing import List


class Solution:
    def pushMin(self, nums: List[int], minQ: deque, i: int):
        while minQ and nums[minQ[-1]] > nums[i]:
            minQ.pop()
        minQ.append(i)

    def pushMax(self, nums: List[int], maxQ: deque, i: int):
        while maxQ and nums[maxQ[-1]] < nums[i]:
            maxQ.pop()
        maxQ.append(i)
    
    def popMin(self, minQ: deque, i: int):
        while minQ and minQ[0] <= i:
            minQ.popleft()

    def popMax(self, maxQ: deque, i: int):
        while maxQ and maxQ[0] <= i:
            maxQ.popleft()
        

    def count(self, nums: List[int], minK: int, maxK: int, i: int, j: int) -> int:
        if not 0 <= i <= j < len(nums):
            return 0
        begin = i
        end = begin - 1
        minQ = deque([])
        maxQ = deque([])
        cnt = 0
        # expand window
        while (end + 1 <= j):
            end += 1
            self.pushMin(nums, minQ, end)
            self.pushMax(nums, maxQ, end)
            # shink when window are valid bound
            while (begin <= end and minQ and maxQ and nums[minQ[0]] == minK and nums[maxQ[0]] == maxK):
                cnt += (j - end + 1)
                self.popMin(minQ, begin)
                self.popMax(maxQ, begin)
                begin += 1
        return cnt

    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        i = 0
        ans = 0
        for j in range(n):
            if not minK <= nums[j] <= maxK:
                ans += self.count(nums, minK, maxK, i, j-1)
                i = j + 1
        return ans + self.count(nums, minK, maxK, i, n-1)
    
# nums = [1,3,5,2,7,5]
# minK = 1
# maxK = 5

nums = [1,1,1,1]
minK = 1
maxK = 1

out = Solution().countSubarrays(nums, minK, maxK)
print(out)
