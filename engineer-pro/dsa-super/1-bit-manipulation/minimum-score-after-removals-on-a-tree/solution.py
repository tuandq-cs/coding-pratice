from typing import List


class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        def calcSubXor(i: int, parI: int):
            if x[i][i] != 0:
                return x[i][i] ^ x[i][parI] if parI != -1 else x[i][i]
            subXor = nums[i]
            for nei in adjList[i]:
                if nei == parI:
                    continue
                x[i][nei] = calcSubXor(nei, i)
                subXor ^= x[i][nei]
            x[i][i] = subXor
            return subXor
            
        n = len(nums)
        adjList = [[] for _ in range(n)]
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        x = [[0]*n for _ in range(n)]
        allXor = 0
        for i in range(n):
            calcSubXor(i, -1)
            allXor ^= nums[i]
        for i in range(len(edges)):
            comp1 = calcSubXor(edges[i][0], edges[i][1])
            comp2 = allXor ^ comp1
            for j in range(i+1, len(edges)):
                comp3 = calcSubXor(edges[j][0], edges[j][1])
                comp4 = allXor ^ comp3
                if comp1 ^ comp3 == comp2 ^ comp4:
                    


        
        
