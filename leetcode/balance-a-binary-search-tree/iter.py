

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def buildArr(self, root, arr):
        if root is None:
            return
        self.buildArr(root.left, arr)
        arr.append(root)
        self.buildArr(root.right, arr)


    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []
        # build arr
        stack = []
        while (stack or root):
            # if current root is not none, push all left-most nodes to stack
            while (root):
                stack.append(root)
                root = root.left
            # take the current left-most in stack
            # Because the pop element has left node is None, so now we just process root, and root.right
            root = stack.pop()
            arr.append(root)
            root = root.right

        # balance from arr
        return self.balance(arr, 0, len(arr)-1)
        
    def balance(self, arr, l, r):
        if l > r:
            return None
        m = l + (r - l) // 2
        root = arr[m]
        root.left = self.balance(arr, l, m-1)
        root.right = self.balance(arr, m+1, r)
        return root
        