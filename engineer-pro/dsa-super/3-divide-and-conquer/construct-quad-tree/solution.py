"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

from typing import List


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        # n == grid.length == grid[i].length
        # n == 2x where 0 <= x <= 6
        n = len(grid) - 1
        return self.solve(grid, [0, n, 0, n])
    def solve(self, grid: List[List[int]], cord: List[int]) -> 'Node': # top, bottom, left, right
        n = len(grid) - 1
        t, b, l, r = cord
        if not(0 <= t <= b <= n and 0 <= l <= r <= n):
            return None
        if t == b or l == r:
            return Node(grid[t][l], True)
        # like post-order
        n = Node(-1, False)
        xM = l + (r - l) // 2
        yM = t + (b - t) // 2
        n.topLeft = self.solve(grid, [t, yM, l, xM])
        n.topRight = self.solve(grid, [t, yM, xM+1, r])
        n.bottomLeft = self.solve(grid, [yM+1, b, l, xM])
        n.bottomRight = self.solve(grid, [yM+1, b, xM+1, r])

        isLeaf = True
        val = n.topLeft.val
        for child in [n.topLeft, n.topRight, n.bottomLeft, n.bottomRight]:
            if not child.isLeaf or val != child.val:
                isLeaf = False
                break
        n.val = val
        n.isLeaf = isLeaf
        if n.isLeaf:
            n.topLeft = None
            n.topRight = None
            n.bottomLeft = None
            n.bottomRight = None
        return n