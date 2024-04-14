from typing import List


class Solution:
    def maxDist(self, ss: int, graph: List[List[int]]) -> int:
        n = len(graph)
        for i in range(n):
            if testBit(ss, i):
                visited = [False] * n
                _, leaf = self.traverse(ss, i, graph, visited)
                for j in range(n):
                    if visited[j] != testBit(ss, j):
                        return 0
                dis, _ = self.traverse(ss, leaf, graph, [False] * n)
                return dis
        return 0
            
    def traverse(self, ss: int, root: int, graph: List[List[int]], visited: List[bool]):
        # set bit at root index
        visited[root] = True
        ans = 0
        leaf = root
        for nei in graph[root]:
            if testBit(ss, nei) and not visited[nei]:
                dis, l = self.traverse(ss, nei, graph, visited)
                if dis + 1 > ans:
                    ans = dis + 1
                    leaf = l
        return ans, leaf
    

    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for (u, v) in edges:
            graph[u-1].append(v-1)
            graph[v-1].append(u-1)
        subsets = []
        for i in range(1, 1 << n):
            subsets.append(i)
        ans = [0] * n
        for ss in subsets:
            dis = self.maxDist(ss, graph)
            ans[dis] += 1
        return ans[1:]
    
def testBit(mask: int, i: int) -> bool:
    return ((mask >> i) & 1) == 1
    

n = 4
edges = [[1,2],[2,3],[2,4]]

n = 5
edges = [[1,5],[2,3],[2,4],[2,5]]
out = Solution().countSubgraphsForEachDiameter(n, edges)
print(out)