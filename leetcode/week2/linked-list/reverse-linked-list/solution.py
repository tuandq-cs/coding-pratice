
from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # return iter(head, None)
        return recur(head, None)


def iter(curNode: Optional[ListNode], prevNode: Optional[ListNode]):
    while (curNode != None):
        tmp = curNode.next
        curNode.next = prevNode
        prevNode = curNode
        curNode = tmp
    return prevNode


def recur(node: Optional[ListNode], prevNode: Optional[ListNode]):
    if node == None:
        return prevNode
    tail = recur(node.next, node)
    node.next = prevNode
    return tail


def debug(head: Optional[ListNode]):
    curNode = head
    out = []
    while (curNode != None):
        out.append(curNode.val)
        curNode = curNode.next
    print(out)


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
result = Solution().reverseList(head)
debug(result)

# Corner case
# 2 nodes
head = ListNode(1, ListNode(2))
result = Solution().reverseList(head)
debug(result)
# empty linked list
head = None
result = Solution().reverseList(head)
debug(result)
