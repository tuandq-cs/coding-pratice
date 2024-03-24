from typing import List

MAXN = 10**5 + 5
primeFactor = [i for i in range(MAXN)]

def sieve():
    p = 2
    while (p*p < MAXN):
        if primeFactor[p] == p:
            for i in range(p*p, MAXN, p):
                primeFactor[i] = p
        p += 1

sieve()


def findFactor(num: int) -> set:
    sFactor = set()
    while num != 1:
        sFactor.add(primeFactor[num])
        num = num // primeFactor[num]
    return sFactor


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        def find(x: int):
            if parent[x] == x: return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(u: int, v: int):
            x = find(u)
            y = find(v)
            if x == y:
                return
            if rank[x] > rank[y]:
                parent[y] = x
            else:
                parent[x] = y
                if rank[x] == rank[y]:
                    rank[y] += 1
        n = len(nums)
        mFactor = {}
        parent = [i for i in range(n)]
        rank = [0 for i in range(n)]

        for i, num in enumerate(nums):
            for factor in findFactor(num):
                if factor in mFactor:
                    union(i, mFactor[factor])
                else:
                    mFactor[factor] = i
        mParent = {}
        for i in range(n):
            p = find(i)
            mParent[p] = mParent.get(p, 0) + 1
        res = 1
        for p in mParent:
            res = max(res, mParent[p])
        return res
