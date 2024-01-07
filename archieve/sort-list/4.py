

from hashlib import new
from math import ceil
from typing import Optional


# SUCCESS, Merge sort with bottom-up approach, space complexity: O(1)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sortList(head: Optional[ListNode]) -> Optional[ListNode]:
    elements = get_elements(head)
    while len(elements) > 1:
        pairs = split_pairs(elements)
        new_elements = []
        for l, r in pairs:
            merged_element = ListNode(0)
            cur = merged_element
            while l or r:
                if l:
                    if r is None or l.val < r.val:
                        cur.next = l
                        l = l.next
                    else:
                        cur.next = r
                        r = r.next
                else:
                    cur.next = r
                    r = r.next
                cur = cur.next
            new_elements.append(merged_element.next)
        elements = new_elements
    return elements[0] if len(elements) == 1 else None

def get_elements(head: Optional[ListNode]):
    cur = head
    elements = []
    while cur != None:
        next = cur.next
        cur.next = None
        elements.append(cur)
        cur = next
    return elements

def split_pairs(elements):
    pairs = []
    for i in range(0, len(elements), 2):
        pair = (elements[i], elements[i+1]) if i + 1 < len(elements) else (elements[i], None)
        pairs.append(pair)
    return pairs

a = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0, ListNode(-10, ListNode(-20)))))))
r = sortList(a)
print(r)
    