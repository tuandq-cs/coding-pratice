# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.globalMax = -1001
        self.recur(root)
        return self.globalMax
        
    def recur(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        gainFromLeft = max(self.recur(node.left), 0)
        gainFromRight = max(self.recur(node.right), 0)
        if node.val + gainFromLeft + gainFromRight > self.globalMax:
            self.globalMax = node.val + gainFromLeft + gainFromRight
        chosenGain = max(gainFromLeft, gainFromRight)
        return node.val + chosenGain

def construct(inp):
    def preOrder(i: int) -> Optional[TreeNode]:
        if i >= len(inp) or inp[i] is None:
            return None
        n = TreeNode(inp[i])
        n.left = preOrder(2*i+1)
        n.right = preOrder(2*i+2)
        return n
    return preOrder(0)

def debug(root: Optional[TreeNode]):
    queue = [root]
    out = []
    while (len(queue) != 0):
        curNode = queue[0]
        queue = queue[1:]
        if curNode is None:
            out.append(None)
            continue
        out.append(curNode.val)
        queue.append(curNode.left)
        queue.append(curNode.right)
    print(out)
        

# inp = [-10,9,20,None,None,15,7]
# root = construct(inp)
# result = Solution().maxPathSum(root)
# print(result)

# I got wrong answer at first
inp = [5,4,8,11,None,13,4,7,2,None,None,None,1]
root = construct(inp)
debug(root)
# result = Solution().maxPathSum(root)
# print(result)


# # Corner cases:
# # 1. All nodes are negative
# inp = [-10,-9,-20,None,None,-15,-7]
# root = construct(inp)
# result = Solution().maxPathSum(root)
# print(result)
# # 2. One node
# inp = [-10]
# root = construct(inp)
# result = Solution().maxPathSum(root)
# print(result)
# # 3. Two nodes
# inp = [-10, 5]
# root = construct(inp)
# result = Solution().maxPathSum(root)
# print(result)
