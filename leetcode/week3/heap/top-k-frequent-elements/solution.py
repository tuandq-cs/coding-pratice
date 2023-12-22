from typing import List
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Build hashmap of frequency
        # Time: O(n)
        # Space: O(n)
        m = {}
        for num in nums:
            if m.get(num) is None:
                m[num] = 0
            m[num] += 1
        # 2. Maintain the size of the heap is only k, if exceed remove the the least freq
        # Time: O(n.log(k))
        h = []
        for num in m:
            heapq.heappush(h, (m[num], num))
            if len(h) > k:  # Release
                heapq.heappop(h)

        # 3. Transform the heap to output
        # Time: O(k.log(k))
        out = [-1] * k
        for i in range(k):
            _, num = heapq.heappop(h)
            out[k-1-i] = num

        return out


nums = [1, 1, 1, 2, 2, 3]
k = 2
out = Solution().topKFrequent(nums, k)
print(out)

nums = [1]
k = 1
out = Solution().topKFrequent(nums, k)
print(out)
