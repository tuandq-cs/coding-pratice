
# https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def oddEvenList(head: Optional[ListNode]) -> Optional[ListNode]:
    start = ListNode(0, head)
    p1 = start.next
    if p1 == None: return None
    p2 = start.next.next if start.next != None else None
    firstP2 = p2
    lastP1 = p1
    while not (p1 == None and p2 == None):
        if p1 != None:
            p1.next = p1.next.next if p1.next != None else None
            p1 = p1.next
            if p1 != None:
                lastP1 = p1
        if p2 != None:
            p2.next = p2.next.next if p2.next != None else None
            p2 = p2.next

    lastP1.next = firstP2
    return start.next
        
a = ListNode(2, ListNode(1, ListNode(3, ListNode(5, ListNode(6, ListNode(4, ListNode(7)))))))
test = oddEvenList(a)
print(test)
        
        
