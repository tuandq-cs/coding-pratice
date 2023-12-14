# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slowPointer = fastPointer = head
        # 1, 1
        while True:
            if fastPointer is None or fastPointer.next is None:
                return False
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next
            if fastPointer == slowPointer:
                return True


tail = ListNode(-4)
pos = ListNode(2, ListNode(0, tail))
tail.next = pos
head = ListNode(3, pos)
# head = [3, 2, 0, -4], pos = 1
# expected: True
res = Solution().hasCycle(head)
print(res)

tail = ListNode(-4)
pos = ListNode(2, ListNode(0, tail))
head = ListNode(3, pos)
# head = [3, 2, 0, -4], pos = -1
# expected: False
res = Solution().hasCycle(head)
print(res)


tail = ListNode(2)
head = ListNode(1, tail)
tail.next = head
# head = [1,2], pos = 0
# expected: True
res = Solution().hasCycle(head)
print(res)

head = ListNode(1)
# head = [1], pos = -1
# expected: False
res = Solution().hasCycle(head)
print(res)
