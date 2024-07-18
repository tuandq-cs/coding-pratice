# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        res = 0
        def dfs(node):
            nonlocal res
            if node is None:
                return [0] * (distance + 1)
            if node.left is None and node.right is None:
                di = [0] * (distance + 1)
                di[1] = 1
                return di
            lDist = dfs(node.left)
            rDist = dfs(node.right)

            for l in range(1, distance):
                for r in range(distance-1, 0, -1):
                    if l + r <= distance:
                        res += lDist[l] * rDist[r]
            # shift
            newDist = [0] * (distance + 1)
            for i in range(1, distance):
                newDist[i+1] = lDist[i] + rDist[i]
            return newDist
        dfs(root)
        return res
