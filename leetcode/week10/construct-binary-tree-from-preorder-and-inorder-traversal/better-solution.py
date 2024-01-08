from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        m = {}
        for i, num in enumerate(inorder):
            m[num] = i

        def helper(preId: int, inStart: int, inEnd: int):
            # Condition here
            if not (0 <= preId < len(preorder)) or not (0 <= inStart <= inEnd < len(inorder)):
                return None
            rootId = m[preorder[preId]]
            numLeftEle = rootId - inStart
            root = TreeNode(preorder[preId])
            root.left = helper(preId+1, inStart, rootId-1)
            root.right = helper(preId+1+numLeftEle, rootId+1, inEnd)
            return root
        return helper(0, 0, len(inorder) - 1)