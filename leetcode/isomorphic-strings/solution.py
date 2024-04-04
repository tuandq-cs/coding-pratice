class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        m = {}
        m2 = {}
        i = 0
        while (i < len(s)):
            if m.get(s[i]) and m[s[i]] != t[i]: return False
            if m2.get(t[i]) and m2[t[i]] != s[i]: return False
            m[s[i]] = t[i]
            m2[t[i]] = s[i]
            i += 1
        return True