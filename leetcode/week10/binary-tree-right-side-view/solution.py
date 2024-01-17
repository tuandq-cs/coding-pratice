from collections import deque
from typing import List, Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        q = deque()
        q.append((0, root))
        while (len(q) != 0):
            level, node = q.popleft()
            if node is None:
                continue
            if level >= len(out):
                out.append(node.val)
            else:
                out[level] = node.val
            q.append((level+1, node.left))
            q.append((level+1, node.right))
        return out
