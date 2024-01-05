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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        out = []

        def solve(node: Optional[TreeNode], level: int):
            if node is None:
                return
            if level >= len(out):
                out.append([])
            out[level].append(node.val)
            solve(node.left, level+1)
            solve(node.right, level+1)
        solve(root, 0)
        return out
