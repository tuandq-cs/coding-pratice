# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def calcHeight(node: Optional[TreeNode]):
            if node is None:
                return 0
            hLeft = calcHeight(node.left)
            hRight = calcHeight(node.right)
            if hLeft == -1 or hRight == -1:
                return -1
            if abs(hLeft - hRight) > 1:
                return -1
            return max(hLeft, hRight) + 1
        return calcHeight(root) != -1