# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        f = s = head
        while (f is not None and f.next is not None):
            f = f.next.next
            s = s.next
            if f == s:
                return True
        return False