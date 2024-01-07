# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        s = []
        pre = None
        while (root != None or len(s) != 0):
            while (root != None):
                s.append(root)
                root = root.left
            root = s.pop()
            if pre is not None and pre.val >= root.val:
                return False
            pre = root
            root = root.right
        return True