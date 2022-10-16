
# https://leetcode.com/problems/longest-common-prefix/

# Solution: https://leetcode.com/problems/longest-common-prefix/discuss/6918/Short-Python-Solution

from typing import List
import heapq

class Prefix:
    def __init__(self, w: str) -> None:
        self.freq = 0
        self.w = w

    def __lt__(self, other):
        if self.freq == other.freq:
            return len(self.w) > len(other.w)
        return self.freq > other.freq

    def inc_freq(self) -> None:
        self.freq += 1

def longestCommonPrefix(strs: List[str]) -> str:
    m = {}
    for str in strs:
        for i in range(len(str)):
            prefix = str[:i+1]
            if not m.get(prefix):
                m[prefix] = Prefix(prefix)
            m[prefix].inc_freq()
    h = []
    for k in m:
        heapq.heappush(h, m[k])
    if len(h) == 0:
        return ""
    r = heapq.heappop(h)
    return r.w if r.freq == len(strs) else ""


strs = ["dog","racecar","car"]
r = longestCommonPrefix(strs)
print(r)
            
        