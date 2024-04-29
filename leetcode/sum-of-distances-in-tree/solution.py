from typing import List


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        adjList = [[] for _ in range(n)]
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        sumDist = [0 for _ in range(n)]
        cnt = [0 for _ in range(n)]

        # post-order, find result for child nodes and then update the root value
        # cuz I update the sumDist and cnt, so I don't return value
        def postOrder(root: int, parent: int):
            for child in adjList[root]:
                if child == parent:
                    continue
                postOrder(child, root)
            # update value for root
            for child in adjList[root]:
                if child == parent:
                    continue
                sumDist[root] += sumDist[child] + cnt[child]
                cnt[root] += cnt[child]
            cnt[root] += 1
            
        postOrder(0, -1)

        # re-rooting: change root -> child
        # because now we have value of root
        # what I gonna do is update value of child
        # so I use pre-order: root -> child nodes
        def preOrder(root: int, parent: int):
            # value of root: sumDist[root]
            for child in adjList[root]:
                if child == parent:
                    continue
                sumDist[child] = sumDist[root] - (cnt[child]) + (n - cnt[child])
                preOrder(child, root)
        
        preOrder(0, -1)
        return sumDist

            



#           2
#     1     5       6
# 3 4 9     7 8     10 0

# sumDist from 2 to [0, 10] exept itself