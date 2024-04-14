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
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        curNode = root
        while True:
            if val < curNode.val:
                if curNode.left is None:
                    curNode.left = TreeNode(val)
                    return root
                curNode = curNode.left
            else:
                if curNode.right is None:
                    curNode.right = TreeNode(val)
                    return root
                curNode = curNode.right
        