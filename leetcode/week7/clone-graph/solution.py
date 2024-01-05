from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        m = {}

        def clone(node: Optional['Node']):
            if node is None:
                return None
            if m.get(node.val) is not None:
                return m[node.val]
            newNode = Node(node.val)
            m[newNode.val] = newNode
            newNeighbors = []
            for n in node.neighbors:
                newNeighbors.append(clone(n))
            newNode.neighbors = newNeighbors
            return newNode
        return clone(node)
