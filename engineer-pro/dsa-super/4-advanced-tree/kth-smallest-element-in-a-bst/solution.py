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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0
        def dfs(node: Optional[TreeNode]):
            nonlocal cnt
            if node is None:
                return -1
            res = dfs(node.left)
            if res != -1:
                return res
            cnt += 1
            if cnt == k:
                return node.val
            return dfs(node.right)
        
        return dfs(root)