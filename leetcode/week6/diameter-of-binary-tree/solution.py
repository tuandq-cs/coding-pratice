

from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxNum = 0

        def solve(node: Optional[TreeNode]):
            nonlocal maxNum
            if node is None:
                return 0
            lNum = solve(node.left)
            rNum = solve(node.right)
            if lNum + rNum + 1 > maxNum:
                maxNum = lNum + rNum + 1
            return max(lNum, rNum) + 1
        solve(root)
        return maxNum - 1
