class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = {}
        for c in s:
            m[c] = m[c] + 1 if m.get(c) is not None else 1
        for c in t:
            if m.get(c) is None:
                return False
            m[c] = m[c] - 1
        for c in m:
            if m[c] != 0:
                return False
        return True


# General case
s = "anagram"
t = "nagaram"
# Expected: True
result = Solution().isAnagram(s, t)
print(result)

s = "rat"
t = "car"
# Expected: False
result = Solution().isAnagram(s, t)
print(result)

# Corner case
s = 'n'
t = 'n'
# Expected: True
result = Solution().isAnagram(s, t)
print(result)
