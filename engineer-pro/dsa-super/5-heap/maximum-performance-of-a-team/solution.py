from typing import List
import heapq

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        pairs = [(efficiency[i], speed[i]) for i in range(n)]
        pairs = sorted(pairs, reverse=True)
    
        perf = 1
        self.pq = []
        curSum = 0
        for i in range(n):
            e, s = pairs[i]
            if len(self.pq) == k:
                v = heapq.heappop(self.pq)
                curSum -= v
            if len(self.pq) < k:
                heapq.heappush(self.pq, s)
                curSum += s
            perf = max(perf, e * curSum)
        return perf % (10**9 + 7)
        # Time complexity: O(n*log(k)), Space: O(n + k)
    
n = 6
speed = [2,10,3,1,5,8]
efficiency = [5,4,3,9,7,2]
k = 2

# pairs = [(9, 1), (7, 5), (5, 2), (4, 10), (3, 3), (2, 8)]
#                                     ^
# curSum = 15
# perf = 15 * 4
# pq = [10, 5]


n = 3
speed = [2,8,2]
efficiency = [2,7,1]
k = 2

# pairs = [(7, 8), (2, 2), (1, 2)]
#                            ^
# curSum = 10
# pq = [8, 2]
# perf = 20
out = Solution().maxPerformance(n, speed, efficiency, k)
print(out)