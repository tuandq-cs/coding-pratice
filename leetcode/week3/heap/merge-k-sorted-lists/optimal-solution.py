from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Time: O(N*log(k))
        # Space: O(log(k)) for recursive stack call
        def merge(l: int, r: int):
            if l > r:
                return None
            if l == r:
                return lists[l]
            m = l + (r - l) // 2
            leftNode = merge(l, m)
            rightNode = merge(m + 1, r)
            return mergeTwoLinkedLists(leftNode, rightNode)

        def mergeTwoLinkedLists(node1: Optional[ListNode], node2: Optional[ListNode]):
            head = ListNode(-1)
            tail = head
            while (node1 != None or node2 != None):
                if node1 == None:
                    tail.next = node2
                    node2 = node2.next
                elif node2 == None:
                    tail.next = node1
                    node1 = node1.next
                else:
                    if node1.val <= node2.val:
                        tail.next = node1
                        node1 = node1.next
                    else:
                        tail.next = node2
                        node2 = node2.next
                tail = tail.next
            return head.next
        return merge(0, len(lists)-1)


def construct(inp: List[List[int]]) -> List[Optional[ListNode]]:
    out = []
    for l in inp:
        head = ListNode(10**5)
        curNode = head
        for i in l:
            newNode = ListNode(i)
            curNode.next = newNode
            curNode = curNode.next
        out.append(head.next)
    return out


def debug(ll: Optional[ListNode]):
    out = []
    curNode = ll
    while curNode != None:
        out.append(curNode.val)
        curNode = curNode.next
    print(out)


lists = [
    [1, 4, 5],
    [1, 3, 4],
    [2, 6]
]
# h = [2, 3, 4]
# out = head -> 1 -> 1
# debug(construct(lists))
out = Solution().mergeKLists(construct(lists))
debug(out)

# lists = []
# out = Solution().mergeKLists(construct(lists))
# debug(out)

# lists = [[]]
# out = Solution().mergeKLists(construct(lists))
# debug(out)
