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
        parent, node = self.findNode(root, key)
        if node is None:
            return root
        maxNode, parMaxNode = self.findMaxNode(node.left)
        if maxNode is not None:
            maxNode.right = node.right
            if maxNode != node.left:
                mi, _ = self.findMinNode(maxNode)
                mi.left = node.left
                # remove maxNode from its parent
                parMaxNode.right = None
            if root == node:
                return maxNode
            if parent.left == node:
                parent.left = maxNode
            else:
                parent.right = maxNode
            return root
        minNode, parMinNode = self.findMinNode(node.right)
        if minNode is not None:
            if minNode != node.right:
                ma, _ = self.findMaxNode(minNode)
                ma.right = node.right
                # remove minNode from its parent
                parMinNode.left = None
            if root == node:
                return minNode
            if parent.left == node:
                parent.left = minNode
            else:
                parent.right = minNode
            return root
        if root == node:
            return None
        if parent.left == node:
            parent.left = None
        else:
            parent.right = None
        return root

    def findNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        curNode = root
        parent = None
        while curNode != None and curNode.val != key:
            parent = curNode
            if key < curNode.val:
                curNode = curNode.left
            else:
                curNode = curNode.right
        return parent, curNode

    def findMinNode(self, node: Optional[TreeNode]):
        if node is None:
            return None, None
        minNode = node
        parMinNode = None

        while minNode.left != None:
            parMinNode = minNode
            minNode = minNode.left 
        return minNode, parMinNode
    
    def findMaxNode(self, node: Optional[TreeNode]):
        if node is None:
            return None, None
        maxNode = node
        parMaxNode = None

        while maxNode.right != None:
            parMaxNode = maxNode
            maxNode = maxNode.right 
        return maxNode, parMaxNode
