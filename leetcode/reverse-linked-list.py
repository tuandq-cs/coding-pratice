
# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    cur = head
    while cur != None:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    return prev

a = ListNode(1, ListNode(2, ListNode(3)))
b = reverseList(a)
print(b)
        