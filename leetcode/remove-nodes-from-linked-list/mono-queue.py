from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def push(self, monoStack: List[ListNode], node: ListNode):
        while len(monoStack) > 0 and monoStack[-1].val < node.val:
            monoStack.pop()
        monoStack.append(node)

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        monoStack = []
        while head:
            self.push(monoStack, head)
            head = head.next
        head = monoStack[0]
        cur = head
        for i in range(1, len(monoStack)):
            cur.next = monoStack[i]
            cur = cur.next
        return head
        # Time: O(n), Space: O(n)