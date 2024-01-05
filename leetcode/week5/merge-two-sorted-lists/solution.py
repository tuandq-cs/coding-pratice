# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        preHead = ListNode(-1)
        curPointer = preHead
        while (list1 and list2):
            if list1.val < list2.val:
                curPointer.next = list1
                list1 = list1.next
            else:
                curPointer.next = list2
                list2 = list2.next
            curPointer = curPointer.next
        if list1 is not None:
            curPointer.next = list1
        else:
            curPointer.next = list2
        return preHead.next

def construct(arr: List[int]) -> Optional[ListNode]:
    dummy = ListNode(-1)
    tail = dummy
    for num in arr:
        tail.next = ListNode(num)
        tail = tail.next
    return dummy.next

def debug(ll: Optional[ListNode]):
    tail = ll
    out = []
    while (tail != None):
        out.append(tail.val)
        tail = tail.next
    print(out)

list1 = [1,2,4]
list2 = [1,3,4]

# 1, 1, 2, 3, 4, 4
ll = Solution().mergeTwoLists(construct(list1), construct(list2))
debug(ll)

list1 = []
list2 = []
ll = Solution().mergeTwoLists(construct(list1), construct(list2))
debug(ll)

list1 = []
list2 = [0]
ll = Solution().mergeTwoLists(construct(list1), construct(list2))
debug(ll)

list1 = [0]
list2 = []
ll = Solution().mergeTwoLists(construct(list1), construct(list2))
debug(ll)