
from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-1)
        curNode = head
        curNode1 = list1
        curNode2 = list2
        # head(-1) -> 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> None
        # curNode = 4 -> None
        # curNode1 = None
        # curNode2 = None
        while (curNode1 is not None or curNode2 is not None):
            if curNode1 is None:
                curNode.next = curNode2
                curNode = curNode2
                curNode2 = curNode2.next
                continue
            if curNode2 is None:
                curNode.next = curNode1
                curNode = curNode1
                curNode1 = curNode1.next
                continue
            if curNode1.val <= curNode2.val:
                curNode.next = curNode1
                curNode = curNode1
                curNode1 = curNode1.next
            else:
                curNode.next = curNode2
                curNode = curNode2
                curNode2 = curNode2.next
        return head.next


def debug(node: Optional[ListNode]):
    curNode = node
    out = []
    while (curNode != None):
        out.append(curNode.val)
        curNode = curNode.next
    print(out)


# input: list1 = [1,2,4], list2 = [1,3,4]
# output: [1,1,2,3,4,4]
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
res = Solution().mergeTwoLists(list1, list2)
debug(res)

# input: list1 = [], list2 = []
# output: []
res = Solution().mergeTwoLists(None, None)
debug(res)

# input: list1 = [], list2 = [0]
# output: [0]
res = Solution().mergeTwoLists(None, ListNode(0))
debug(res)
