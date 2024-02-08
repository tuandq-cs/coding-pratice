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
        node = self.findNode(root, key)
        if node is None:
            return root
        _, leftMax = self.dfs(node.left)
        if leftMax is not None:
            tmp = leftMax.val
            self.removeLeafNode(node, tmp)
            node.val = tmp
            return root
        rightMin, _ = self.dfs(node.right)
        if rightMin is not None:
            tmp = rightMin.val
            self.removeLeafNode(node, tmp)
            node.val = tmp
            return root
        # node is leaf
        return self.removeLeafNode(root, node.val)


    def findNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        curNode = root
        while curNode != None and curNode.val != key:
            if key < curNode.val:
                curNode = curNode.left
            else:
                curNode = curNode.right
        return curNode

    def dfs(self, node: Optional[TreeNode]):
        if node is None:
            return None, None
        minNode = maxNode = node
        leftMin, _ = self.dfs(node.left)
        if leftMin is not None:
            minNode = leftMin
        _, rightMax = self.dfs(node.right)
        if rightMax is not None:
            maxNode = rightMax
        return minNode, maxNode
    
    def removeLeafNode(self, node: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curNode = node
        prev = None
        while curNode.val != val:
            prev = curNode
            if val < curNode.val:
                curNode = curNode.left
            else:
                curNode = curNode.right
        # Node is also root
        if prev is None:
            return None
        if prev.left == curNode:
            prev.left = None
            return node
        if prev.right == curNode:
            prev.right = None
            return node
        return None