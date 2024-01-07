# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        sVersion = 0
        while (l <= r):
            m = l + (r - l) // 2
            if isBadVersion(m):
                r = m - 1
                sVersion = m
            else:
                l = m + 1
        return sVersion