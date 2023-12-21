import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        # Time: O(N.log(N)), N is num of points
        for point in points:
            x, y = point
            squareDist = x**2 + y ** 2
            heapq.heappush(h, (squareDist, [x, y]))
        out = []
        # Time: O(k), 1 <= k <= N
        for _ in range(k):
            _, cord = heapq.heappop(h)
            out.append(cord)
        # Overall time: O(N.log(N) + O(k)) => O(N.log(N))
        return out


points = [[1, 3], [-2, 2]]
k = 1
out = Solution().kClosest(points, k)
print(out)

points = [[3, 3], [5, -1], [-2, 4]]
k = 2
out = Solution().kClosest(points, k)
print(out)

points = [[3, 3]]
k = 1
out = Solution().kClosest(points, k)
print(out)
