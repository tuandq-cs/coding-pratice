import stat
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            if u == v:
                return False
            adjList[v].append(u)
        state = [0] * numCourses
        # 0: not visited
        # 1: processing
        # 2: processed
        for i in range(numCourses):
            if state[i] == 2:
                continue
            if self.dfs(i, adjList, state) is False:
                return False
        for i in range(numCourses):
            if state[i] == 0:
                return False
        return True

    def dfs(self, i: int, adjList: List[List[int]], state: List[int]):
        if state[i] == 1:
            return False
        state[i] = 1
        for nei in adjList[i]:
            if state[nei] == 2:
                continue
            if self.dfs(nei, adjList, state) is False:
                return False
        state[i] = 2
        return True