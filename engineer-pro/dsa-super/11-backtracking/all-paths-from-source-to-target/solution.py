from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        self.dfs(0, graph, [0], ans)
        return ans
        
    def dfs(self, idx: int, graph: List[List[int]], path: List[int], ans: List[List[int]]):
        if idx == len(graph) - 1:
            ans.append(path.copy())
            return
        for n in graph[idx]:
            path.append(n)
            self.dfs(n, graph, path, ans)
            path.pop()
        return