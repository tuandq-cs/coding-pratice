from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # l = []
        # for num in nums:
        #     heapq.heappush(l, num)
        # for _ in range(len(nums) - k):
        #     heapq.heappop(l)
        # return heapq.heappop(l)
        heapq.heapify(nums)
        return heapq.nlargest(k, nums)[-1]


nums = [3, 2, 1, 5, 6, 4]
k = 2
r = Solution().findKthLargest(nums, k)
print(r)

nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
r = Solution().findKthLargest(nums, k)
print(r)

nums = [6]
k = 1
r = Solution().findKthLargest(nums, k)
print(r)
