base = 256
mod = 10**9 + 7

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle): return -1
        needleH = 0
        haystackH = 0
        n = len(haystack)
        m = len(needle)
        for i in range(m):
            needleH = (needleH * base + ord(needle[i])) % mod
            haystackH = (haystackH * base + ord(haystack[i])) % mod
        if needleH == haystackH:
            return 0
        for i in range(1, n-m+1):
            haystackH = (haystackH * base + ord(haystack[i+m-1])) % mod
            haystackH = (haystackH - ord(haystack[i-1])* base**m + mod) % mod
            if needleH == haystackH:
                return i
        return -1