# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        # [4, 1, 1, 9]
        #        ^
        # shift val to right 1 unit, then delete the last node (tail)
        while node:
            node.val = node.next.val
            if (node.next.next is None):
                node.next = None
            node = node.next
        