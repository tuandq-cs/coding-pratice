from typing import List


class Solution:
    def maxDist(self, n: int, mask: int, adjList: List[List[int]]) -> int:
        u = 0
        while (u < n):
            if testBit(mask, u):
                break
            u += 1
        # dfs 1st time
        depth = [-1 for _ in range(n)]
        depth[u] = 0
        self.dfs(u, mask, adjList, depth)
        # choose node has largest depth and validate whether mask is valid
        v = 0
        cnt = 0
        for i in range(n):
            if depth[i] >= 0: cnt += 1
            if depth[i] > depth[v]: v = i
        if cnt != mask.bit_count():
            return -1
        # dfs 2nd time
        depth = [-1 for _ in range(n)]
        depth[v] = 0
        self.dfs(v, mask, adjList, depth)
        return max(depth)
    
    def dfs(self, u: int, mask: int, adjList: List[List[int]], depth: List[int]):
        for v in adjList[u]:
            if testBit(mask, v) and depth[v] < 0:
                depth[v] = 1 + depth[u]
                self.dfs(v, mask, adjList, depth)
            


    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        adjList = [[] for _ in range(n)]
        for u, v in edges:
            adjList[u-1].append(v-1)
            adjList[v-1].append(u-1)
        
        ans = [0] * n
        for mask in range(1, 1 << n):
            dis = self.maxDist(n, mask, adjList)
            if dis != -1:
                ans[dis] += 1
        return ans[1:]
    
def testBit(mask: int, i: int) -> int:
    return (mask >> i) & 1