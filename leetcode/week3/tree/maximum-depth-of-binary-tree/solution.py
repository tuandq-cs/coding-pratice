
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def recur(node: Optional[TreeNode], level: int):
            if node is None:
                return level
            return max(recur(node.left, level+1), recur(node.right, level+1))
        
        def iter(root: Optional[TreeNode]):
            maxLevel = 0
            nodeStacks = [root]
            levelStacks = [0]
            while (len(nodeStacks) != 0):
                curNode = nodeStacks.pop()
                curLevel = levelStacks.pop()
                if curNode is None:
                    continue
                if curLevel + 1 > maxLevel:
                    maxLevel = curLevel + 1
                levelStacks.append(curLevel+1)
                nodeStacks.append(curNode.left)
                levelStacks.append(curLevel+1)
                nodeStacks.append(curNode.right)
            return maxLevel
        return iter(root) 
        # return recur(root, 0)

def construct(inp) -> Optional[TreeNode]:
    def preOrder(i: int) -> Optional[TreeNode]:
        if i >= len(inp):
            return None
        node = TreeNode(inp[i])
        node.left = preOrder(2*i+1)
        node.right  = preOrder(2*i+2)
        return node
    return preOrder(0)

inp = [3,9,20,None,None,15,7]
root = construct(inp)
#       3, i = 0
#   9, i = 1    20, i = 2
# None None    15, i= 5, 7, i=6
result = Solution().maxDepth(root)
# expected: 3
print(result)

inp = [1,None,2]
root = construct(inp)
result = Solution().maxDepth(root)
print(result)

