# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None or q is None:
            return p is None and q is None
        if p.val != q.val:
            return False
        if not self.isSameTree(p.left, q.left):
            return False
        if not self.isSameTree(p.right, q.right):
            return False
        return True

def construct(inp):
    def preOrder(i: int) -> Optional[TreeNode]:
        if i >= len(inp):
            return None
        n = TreeNode(inp[i])
        n.left = preOrder(2*i+1)
        n.right = preOrder(2*i+2)
        return n
    return preOrder(0)

p = [1,2,3]
q = [1,2,3]
result = Solution().isSameTree(construct(p), construct(q))
print(result)

p = [1,2]
q = [1,None,2]
result = Solution().isSameTree(construct(p), construct(q))
print(result)

p = [1,2,1]
q = [1,1,2]
result = Solution().isSameTree(construct(p), construct(q))
print(result)