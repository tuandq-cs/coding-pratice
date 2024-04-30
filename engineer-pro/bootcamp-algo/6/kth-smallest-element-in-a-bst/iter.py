from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # in-order
        stack = [] # stack here mean nodes from left subtree of the high level node
        cnt = 0
        while len(stack) > 0 or root:
            # put all left nodes of current root to stack
            # keep high level root to later processing
            while root != None:
                stack.append(root)
                root = root.left
            # every time I pop node from stack, that mean I already process all left nodes of the poped node
            root = stack.pop()
            cnt += 1
            if cnt == k:
                return root.val
            root = root.right
        return -1

            