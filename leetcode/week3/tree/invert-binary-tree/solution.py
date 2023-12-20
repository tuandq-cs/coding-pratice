# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def recur(root: Optional[TreeNode]) -> Optional[TreeNode]:
            if root is None:
                return None
            tmp = self.recur(root.left)
            root.left = self.recur(root.right)
            root.right = tmp
            return root
    
        def iter(root: Optional[TreeNode]) -> Optional[TreeNode]:
            stacks = [root]
            while len(stacks) != 0:
                curNode = stacks.pop()
                if curNode is None:
                    continue
                stacks.append(curNode.right)
                stacks.append(curNode.left)
                tmp = curNode.left
                curNode.left = curNode.right
                curNode.right = tmp
            return root
        return iter(root)

def construct(inp) -> Optional[TreeNode]:
    def preOrder(i: int) -> Optional[TreeNode]:
        if i >= len(inp):
            return None
        n = TreeNode(inp[i])
        n.left = preOrder(2*i+1)
        n.right = preOrder(2*i+2)
        return n
    return preOrder(0)

def debug(root: Optional[TreeNode]):
    queue = Queue()
    queue.put(root)
    out = []
    while (queue.qsize() != 0):
        n = queue.get()
        if n is None:
            continue
        out.append(n.val)
        queue.put(n.left)
        queue.put(n.right)
    print(out)


inp = [4,2,7,1,3,6,9]
root = construct(inp)
#                  root = 4, i = 0
#       7 , i = 2                   2, i = 1               
#   9, i = 6   6, i = 5        3, i = 4  1, i = 3       
result = Solution().invertTree(root)
debug(result)

inp = [2,1,3]
root = construct(inp)
result = Solution().invertTree(root)
debug(result)

inp = []
root = construct(inp)
result = Solution().invertTree(root)
debug(result)


