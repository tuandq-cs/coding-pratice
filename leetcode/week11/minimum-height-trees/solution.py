from typing import List
import heapq


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        memo = [None for _ in range(n)]
        parent = [-1 for _ in range(n)]

        def getHeight(i: int, parentI: int) -> int:
            if memo[i] is None:
                maxHeap = []

                for nei in neighbors[i]:
                    if nei == parentI:
                        continue
                    h = getHeight(nei, i)
                    heapq.heappush(maxHeap, (-h, nei))
                parent[i] = parentI
                memo[i] = maxHeap

            else:
                if parent[i] != -1:
                    pHeight = getHeight(parent[i], i)
                    heapq.heappush(memo[i], (-pHeight, parent[i]))
                    parent[i] = -1
            if len(memo[i]) == 0:
                return 1

            h, j = memo[i][0]
            if j == parentI:
                cop = memo[i].copy()
                heapq.heappop(cop)
                if len(cop) == 0:
                    return 1
                h, _ = cop[0]
            return -h + 1

        neighbors = [[] for _ in range(n)]
        for (a, b) in edges:
            neighbors[a].append(b)
            neighbors[b].append(a)
        result = []
        minHeight = n
        for i in range(n):
            h = getHeight(i, -1)
            if h < minHeight:
                minHeight = h
                result = [i]
            elif h == minHeight:
                result.append(i)
        # Time: O(N*logN), Space: O(N*N)
        return result


n = 4
edges = [[1, 0], [1, 2], [1, 3]]
out = Solution().findMinHeightTrees(n, edges)
print(out)

n = 6
edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
out = Solution().findMinHeightTrees(n, edges)
print(out)
