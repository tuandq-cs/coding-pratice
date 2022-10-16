
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Solution: https://leetcode.com/problems/remove-nth-node-from-end-of-list/discuss/8804/Simple-Java-solution-in-one-pass

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# My solution
# def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
#     if head.next == None:
#         return None
#     p2 = head.next
#     l = 1
#     # 1 2 3 4 5 6 7 None
#     while p2 != None:
#         if p2.next != None:
#             p2 = p2.next.next 
#             l += 2
#         else:
#             p2 = p2.next
#             l += 1
#     i1 = 0
#     p1 = head
#     if l - n == 0:
#         return p1.next
#     while i1 < l - 1 - n:
#         p1 = p1.next
#         i1 += 1
#     p1.next = p1.next.next if p1.next != None else None
#     return head

# Solution: https://leetcode.com/problems/remove-nth-node-from-end-of-list/discuss/8804/Simple-Java-solution-in-one-pass

def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    start = ListNode(0)
    slow = start
    fast = start
    start.next = head
    for _ in range(n+1):
        fast = fast.next
    while fast != None:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return start.next

a = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
removeNthFromEnd(a, 3)