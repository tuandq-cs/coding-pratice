# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            tmp = p
            p = q
            q = tmp
        curNode = root
        # 1 <= 2 <= 2
        while not(p.val <= curNode.val <= q.val):
            if curNode.val < p.val:
                curNode = curNode.right
            else:
                curNode = curNode.left
        return curNode
    
def construct(inp) -> TreeNode:
    def preOrder(i: int) -> TreeNode:
        if i >= len(inp):
            return None
        n = TreeNode(inp[i])
        n.left = preOrder(2*i+1)
        n.right = preOrder(2*i+2)
        return n
    return preOrder(0)

inp = [6,2,8,0,4,7,9,None,None,3,5]
root = construct(inp)
p = TreeNode(5)
q = TreeNode(0)
result = Solution().lowestCommonAncestor(root, p, q)
print(result.val)

inp = [6,2,8,0,4,7,9,None,None,3,5]
root = construct(inp)
p = TreeNode(2)
q = TreeNode(8)
result = Solution().lowestCommonAncestor(root, p, q)
print(result.val)

inp = [2, 1]
root = construct(inp)
p = TreeNode(2)
q = TreeNode(1)
result = Solution().lowestCommonAncestor(root, p, q)
print(result.val)
