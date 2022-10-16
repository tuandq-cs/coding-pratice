
from typing import Optional, Tuple

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# SUCCESS: Merge sort top-down approach
def sortList(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None or head.next is None:
        return head
    left, right = splitHalf(head)
    left = sortList(left)
    right = sortList(right)
    
    merged_list = ListNode(0)
    cur = merged_list
    while left or right:
        if left:
            if right is None or left.val < right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
        else:
            cur.next = right
            right = right.next
        cur = cur.next
    return merged_list.next


def splitHalf(head: ListNode) -> Tuple[Optional[ListNode], Optional[ListNode]]:
    t = ListNode(0, head)
    fast = t
    slow = t
    while fast != None and fast.next != None:
        fast = fast.next.next if fast.next else None
        slow = slow.next
    second_part = slow.next
    slow.next = None
    return (head, second_part)

# 2, 1, 3, 5, 6, 4, 7
# -1,5,3,4,0
a = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0, ListNode(-10, ListNode(-20)))))))
r = sortList(a)
print(r)