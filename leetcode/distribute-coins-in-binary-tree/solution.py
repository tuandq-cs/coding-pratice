from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getBalance(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        leftBal = self.getBalance(root.left)
        rightBal = self.getBalance(root.right)
        self.moves += abs(leftBal) + abs(rightBal)
        return leftBal + rightBal + (root.val - 1)
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0
        self.getBalance(root)
        return self.moves
    
