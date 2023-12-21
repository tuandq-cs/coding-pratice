# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List, Optional
import heapq


# Priority Queue Approach

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 1. Build a priority queue with k elements
        # 2. Get the min node and link to the output linked list
        # 3. Replace the min node with the latest node, remove the min node and add the next's min node (if not None)
        # 4. Heapify and repeat the 2 for all nodes until the queue is empty
        k = len(lists)
        h = []
        # Time: O(k.log(k))
        for i in range(k):
            if lists[i] is None:
                continue
            heapq.heappush(h, (lists[i].val, i))
        out = ListNode(10**5)
        curOut = out
        # Time: O(N.log(k))
        while (len(h) != 0):
            _, i = heapq.heappop(h)
            m = lists[i]
            curOut.next = m
            curOut = curOut.next
            if m.next != None:
                heapq.heappush(h, (m.next.val, i))
            lists[i] = m.next
        # Overall time: O(k.log(k)) + O(N.log(k)) -> O(N.log(k)), Space: O(k)
        return out.next


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

lists = []
out = Solution().mergeKLists(construct(lists))
debug(out)

lists = [[]]
out = Solution().mergeKLists(construct(lists))
debug(out)
