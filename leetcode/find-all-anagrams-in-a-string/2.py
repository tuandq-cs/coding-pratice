

from queue import Queue
from typing import List


def findAnagrams(s: str, p: str) -> List[int]:
    c_dict = {}
    diff = {}
    for c in p:
        c_dict[c] = (c_dict.get(c) or 0) + 1
        diff[c] = (diff.get(c) or 0) + 1

    q = Queue(maxsize=len(p))
    r = []
    i = 0
    for c in s:
        if q.full():
            pop_ele = q.get()
            if c_dict.get(pop_ele):
                diff[pop_ele] = (diff.get(pop_ele) or 0) + 1
                if diff[pop_ele] == 0:
                    del diff[pop_ele]

        q.put(c)
        if c_dict.get(c):
            diff[c] = (diff.get(c) or 0) - 1
            if diff[c] == 0:
                del diff[c]
        if len(diff) == 0:
            r.append(i - len(p) + 1)
        i += 1
    return r


s = "cbaebabacd"
p = "abc"
# s = "abab"
# p = "ab"
r = findAnagrams(s, p)
print(r)

            