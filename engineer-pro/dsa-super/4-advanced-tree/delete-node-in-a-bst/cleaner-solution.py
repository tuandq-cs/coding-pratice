# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        maxNode = self.findMaxNode(root.left)
        maxNode.left = self.deleteNode(root.left, maxNode.val)
        maxNode.right = root.right
        return maxNode
    
    def findMaxNode(self, root: Optional[TreeNode]):
        maxNode = root
        while maxNode.right is not None:
            maxNode = maxNode.right
        return maxNode