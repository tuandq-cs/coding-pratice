from typing import List


class Solution:

    def equationsPossible(self, equations: List[str]) -> bool:
        def find(x: int) -> int:
            if x == parent[x]: return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(u: int, v: int) -> bool:
            x = find(u)
            y = find(v)
            if x == y:
                return False
            if rank[x] > rank[y]:
                parent[y] = x
            else:
                parent[x] = y
                if rank[x] == rank[y]:
                    rank[y] += 1
            return True
        parent = [i for i in range(27)]
        rank = [0 for _ in range(27)]
        for eq in equations:
            if eq[1] == '=':
                u = ord(eq[0]) - ord('a')
                v = ord(eq[3]) - ord('a')
                union(u, v)
        for eq in equations:
            if eq[1] == '!':
                u = ord(eq[0]) - ord('a')
                v = ord(eq[3]) - ord('a')
                x = find(u)
                y = find(v)
                if x == y:
                    return False
        return True