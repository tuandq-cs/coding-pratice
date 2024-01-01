class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = {}
        for c in s:
            if counter.get(c) is None:
                counter[c] = 0
            counter[c] += 1
        for c in t:
            if counter.get(c) is None:
                return False
            counter[c] -= 1
        for c in counter:
            if counter[c] != 0:
                return False
        return True