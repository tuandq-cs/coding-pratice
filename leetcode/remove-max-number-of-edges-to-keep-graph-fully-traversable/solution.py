from typing import List


class Solution:
    # https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/solutions/831573/python-union-find
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        def find(u):
            if u != root[u]:
                root[u] = find(root[u])
            return root[u]

        def union(u, v):
            rU, rV = find(u), find(v)
            if rU == rV: return 0
            root[rU] = rV
            return 1

        # union find
        root = [i for i in range(n+1)]
        eAlice, eBob = 0, 0
        res = 0

        # Process type 3 first
        for t,u,v in edges:
            if t == 3:
                if union(u, v):
                    eAlice += 1
                    eBob += 1
                else:
                    res += 1
        tmp = root.copy()
        # Process Alice
        for t,u,v in edges:
            if t == 1:
                if union(u, v):
                    eAlice += 1
                else:
                    res += 1
        root = tmp
        # Process Bob
        for t,u,v in edges:
            if t == 2:
                if union(u, v):
                    eBob += 1
                else:
                    res += 1
        
        # eAlice, eBob must = n - 1
        return res if eAlice == eBob == n - 1 else -1 
        
        