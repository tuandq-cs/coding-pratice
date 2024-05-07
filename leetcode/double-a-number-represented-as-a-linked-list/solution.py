from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        return prev

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = self.reverse(head)
        residual = 0
        cur = head
        while cur:
            v = (cur.val * 2 + residual) % 10
            residual = (cur.val * 2 + residual) // 10
            cur.val = v
            cur = cur.next
        head = self.reverse(head)
        if residual:
            head = ListNode(residual, head)
        return head
            
        