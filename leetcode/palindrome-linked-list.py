

# https://leetcode.com/problems/palindrome-linked-list/
# https://leetcode.com/problems/palindrome-linked-list/solution/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head: Optional[ListNode]) -> bool:
    frontPointer = ListNode(head.val, head.next)
    frontIndex = 0
    def reverseLinkedList(curNode: Optional[ListNode], curIndex = 0) -> bool:
        nonlocal frontPointer, frontIndex
        if curNode is None:
            return True
        if reverseLinkedList(curNode.next, curIndex + 1) == False:
            return False
        if frontIndex >= curIndex:
            return True
        if curNode.val != frontPointer.val:
            return False
        frontPointer = frontPointer.next
        frontIndex += 1
        return True        
    return reverseLinkedList(head, 0)


# def isPalindrome(head: Optional[ListNode]) -> bool:
#     lenll = lenOfLinkedList(head)
#     cur = head
#     curI = 0
#     s = []
#     while cur != None:
#         isPop = curI >= lenll // 2
#         if lenll % 2 and curI == lenll // 2:
#                 s.append(cur.val)
#         if isPop:
#             if cur.val != s.pop():
#                 return False
#         else:
#             s.append(cur.val)
#         curI += 1
#         cur = cur.next
#     return True


# def lenOfLinkedList(head: Optional[ListNode]) -> int:
#     l = 0
#     cur = head
#     while cur != None:
#         l += 1
#         cur = cur.next
#     return l

a = ListNode(1, ListNode(2, ListNode(2, ListNode(2, ListNode(1)))))
print(isPalindrome(a))