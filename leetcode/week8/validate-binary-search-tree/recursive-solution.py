# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def recur(root: Optional[TreeNode], minValue, maxValue):
            if root is None:
                return True
            if not (minValue < root.val < maxValue):
                return False
            return recur(root.left, minValue, root.val) and recur(root.right, root.val, maxValue)
        return recur(root, float('-inf'), float('inf'))