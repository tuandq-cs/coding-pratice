


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
        self.buildArr(root, arr)

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
        