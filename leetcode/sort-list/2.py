

# Definition for singly-linked list.
from typing import List, Optional
import heapq

# Put to a heapq, time complexity O(nlogn), space complexity O(n)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sortList(head: Optional[ListNode]) -> Optional[ListNode]:
    l = []
    while head != None:
        heapq.heappush(l, head.val)
        head = head.next
    
    head = ListNode(0)
    cur = head
    while len(l):
        cur.next = ListNode(heapq.heappop(l))
        cur = cur.next
    return head.next


# -1,5,3,4,0
a = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))
r = sortList(a)
print(r)
