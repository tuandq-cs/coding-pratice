# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        out = []
        def dfs(node: Optional[TreeNode], s: List[int]):
            if node is None:
                return
            s.append(node.val)
            # leaf node
            if node.left is None and node.right is None:
                out.append(s.copy())
            else:
                dfs(node.left, s)
                dfs(node.right, s)
            s.pop()

        dfs(root, [])
        s = 0
        for p in out:
            for i, num in enumerate(p):
                s += num * 10**(len(p) - 1 - i)
        return s