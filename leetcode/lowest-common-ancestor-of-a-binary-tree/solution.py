# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(cur, dest, level, ancestor):
            if cur is None:
                return False
            ancestor[level] = cur
            if cur == dest:
                return True
            if dfs(cur.left, dest, level+1, ancestor) or dfs(cur.right, dest, level+1, ancestor):
                return True
            ancestor[level] = None
            return False
        maxLevel = 10000 + 3
        anP = [None] * maxLevel
        dfs(root, p, 0, anP)
        anQ = [None] * maxLevel
        dfs(root, q, 0, anQ)
        for i in range(maxLevel-1, -1, -1):
            if anP[i] is None or anQ[i] == None:
                continue
            if anP[i] == anQ[i]:
                return anP[i]
        return root

