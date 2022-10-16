
# https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
from typing import Optional

## FAILED cause: O(n^2) in worse case.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sortList(head: Optional[ListNode]) -> Optional[ListNode]:
    # 0, -1, None
    if head == None:
        return None
    pivot = head # 0
    p1 = None # -1, None
    p2 = None # None
    cur = pivot.next # None
    while cur != None:
        tmp = cur.next
        if cur.val > pivot.val:
            cur.next = p2
            p2 = cur
        else:
            cur.next = p1
            p1 = cur
        cur = tmp

    s1 = sortList(p1) # -1, None
    s2 = sortList(p2) # None
    pivot.next = s2 # 0, None
    r = pushListToList(s1, pivot)
    return r # -1, 0, None

def pushListToList(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    if l1 == None:
        return l2
    cur = l1
    while cur.next != None:
        cur = cur.next
    cur.next = l2
    return l1
# [3,5,-1,4,0]
# -1,5,3,4,0
a = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0, None)))))
b = sortList(a)
print(b)
