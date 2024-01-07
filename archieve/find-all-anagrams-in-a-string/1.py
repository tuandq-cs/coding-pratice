
# https://leetcode.com/problems/find-all-anagrams-in-a-string


from re import T
from typing import List


# Failed: Time Limit Exceeded

def findAnagrams(s: str, p: str) -> List[int]:
    i = 0
    r = []
    while i + len(p) <= len(s):
        if is_anagram(s[i:i+len(p)], p):
            r.append(i)
        i += 1
    return r

def is_anagram(s1, s2):
    c_dict = {}
    for c in s1:
        c_dict[c] = c_dict[c] if c_dict.get(c) else 0
        c_dict[c] += 1
    for c in s2:
        if c_dict.get(c) is None:
            return False
        c_dict[c] -= 1
    for c in c_dict:
        if c_dict.get(c) != 0:
            return False
    return True

# s = "cbaebabacd"
# p = "abc"

s = "abab"
p = "ab"
r = findAnagrams(s, p)
print(r)