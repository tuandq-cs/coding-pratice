from typing import List


base = 256
mod = 10**9 + 7

def getHash(s: str) -> List[int]:
    n = len(s)
    h = [0] * (n+1)
    for i in range(1, n+1):
        h[i] = (h[i-1] * base + ord(s[i-1])) % mod
    return h

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle): return -1
        needleH = getHash(needle)
        haystackH = getHash(haystack)
        k = len(needle)
        n = len(haystack)
        powerk = pow(base, k, mod)

        for i in range(n-k+1):
            sub_hash = (haystackH[i+k] - (haystackH[i] * powerk) % mod + mod) % mod
            if sub_hash == needleH[-1]:
                return i
        return -1

        # 123456
        #-123000
