from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        m = {}
        for i, num in inorder:
            m[num] = i

        def helper(preId: int, inStart: int, inEnd: int):
            # Condition here
            rootId = m[preorder[preId]]
            numLeftEle = rootId - inStart
            root = TreeNode(preorder[preId])
            root.left = helper(preId+1, inStart, rootId-1)
            root.right = helper(preId+numLeftEle, rootId+1, inEnd)
            