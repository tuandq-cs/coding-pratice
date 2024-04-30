from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0
        def dfs(root: Optional[TreeNode]):
            nonlocal cnt
            if root is None:
                return -1
            v = dfs(root.left)
            if cnt == k:
                return v
            cnt += 1
            if cnt == k:
                return root.val
            return dfs(root.right)
        return dfs(root)
            