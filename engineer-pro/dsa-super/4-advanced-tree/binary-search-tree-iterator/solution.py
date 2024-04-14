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

class LinkedListNode:
    def __init__(self, treeNode: TreeNode, next=None) -> None:
        self.treeNode = treeNode
        self.next = next

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        head, tail = self.dfs(root)
        self.head = head
        self.tail = tail
        self.cur = head

    def dfs(self, node: Optional[TreeNode]) -> (Optional[LinkedListNode], Optional[LinkedListNode]):
        if node is None:
            return None, None
        llNode = LinkedListNode(node)
        minNode = maxNode = llNode
        leftMin, leftMax = self.dfs(node.left)
        if leftMax is not None:
            leftMax.next = llNode
        if leftMin is not None:
            minNode = leftMin
        rightMin, rightMax = self.dfs(node.right)
        llNode.next = rightMin
        if rightMax is not None:
            maxNode = rightMax
        return minNode, maxNode


    def next(self) -> int:
        res = self.cur.treeNode.val
        self.cur = self.cur.next
        return res

    def hasNext(self) -> bool:
        return self.cur != None


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()