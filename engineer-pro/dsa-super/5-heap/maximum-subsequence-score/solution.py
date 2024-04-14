from typing import List
import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [(nums2[i], nums1[i]) for i in range(len(nums2))]
        pairs = sorted(pairs, reverse=True)
        ans = 0
        pq = []
        curSum = 0
        for n2, n1 in pairs:
            if len(pq) == k and n1 > pq[0]:
                v = heapq.heappop(pq)
                curSum -= v
            if len(pq) < k:
                heapq.heappush(pq, n1)
                curSum += n1
            if len(pq) == k and n2 * curSum > ans:
                ans = n2 * curSum
        return ans
    
nums1 = [1,3,3,2]
nums2 = [2,1,3,4]
k = 3
# nums2 = [(4,3),(3,2),(2,0),(1,1)]
# curSum = 5
# pq = [3, 2]
# ans = 15

nums1 = [4,2,3,1,1]
nums2 = [7,5,10,9,6]
k = 1
out = Solution().maxScore(nums1, nums2, k)
print(out)
