# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        # dfs
        # return 0: need cover
        # return 1: camera on
        # return 2: covered, not have camera
        res = 0
        def dfs(root: Optional[TreeNode]):
            nonlocal res
            if root is None:
                return 2
            if root.left is None and root.right is None:
                return 0
            lV = dfs(root.left)
            rV = dfs(root.right)
            if lV == 0 or rV == 0: # one of child need cover, will put camera on this node
                res += 1
                return 1
            # lV in (1, 2), rV in (1, 2)
            # if children is covered (not have camera), this one will should be need cover
            return 2 if lV == 1 or rV == 1 else 0
        return res + 1 if dfs(root) == 0 else res # the root need cover, but root has no parent, so it have to cover itself
        
        