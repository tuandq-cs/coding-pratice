# Definition for a binary tree node.

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        def recur(node: Optional[TreeNode]):
            if node is None:
                return
            recur(node.left)
            out.append(node.val)
            recur(node.right)
            return
        
        def iter(node: Optional[TreeNode]):
            s = []
            while node != None or len(s) != 0:
                while (node != None):
                    s.append(node)
                    node = node.left
                node = s.pop()
                out.append(node.val)
                node = node.right
            return


        iter(root)
        return out