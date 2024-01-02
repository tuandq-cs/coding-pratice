class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p
        curNode = root
        while not (p.val <= curNode.val <= q.val):
            if curNode.val < p.val:
                curNode = curNode.right
            else:
                curNode = curNode.left
        return curNode