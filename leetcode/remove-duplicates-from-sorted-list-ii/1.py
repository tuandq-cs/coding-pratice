

# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    s = ListNode(-101, head)

    unique_pointer = s
    cur_pointer = head

    num_val = 0
    prev = s
    while cur_pointer != None:
        if cur_pointer.val != prev.val:
            if num_val == 1:
                unique_pointer.next = prev
                unique_pointer = unique_pointer.next
            num_val = 1
        else:
            num_val +=1 
        prev = cur_pointer
        cur_pointer = cur_pointer.next
    if num_val == 1:
        unique_pointer.next = prev
        unique_pointer = unique_pointer.next
    unique_pointer.next = None
    return s.next

# [1,2,3,3,4,4,5]
a = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4, ListNode(5, ListNode(5))))))))
r = deleteDuplicates(a)
print(r) 