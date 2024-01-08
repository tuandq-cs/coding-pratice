# Definition for a binary tree node.

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Overall time: O(n*log(n))


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.construct(preorder, inorder)

    def construct(self, preorder: List[int], inorder: List[int]):
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        # Find rootIdx within inorder
        # Time: O(n), n is total number of nodes
        rootIdx = self.findRootIdx(preorder[0], inorder)
        root = TreeNode(preorder[0])

        root.left = self.buildTree(preorder[1:1+rootIdx], inorder[:rootIdx])
        if rootIdx + 1 < len(preorder):
            root.right = self.buildTree(
                preorder[1+rootIdx:], inorder[rootIdx+1:])
        return root

    def findRootIdx(self, val: int, inorder: List[int]):
        for i, num in enumerate(inorder):
            if num == val:
                return i


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
t = Solution().buildTree(preorder, inorder)
