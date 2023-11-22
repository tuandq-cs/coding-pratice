class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteTable = {}
        for ch in ransomNote:
            ransomNoteTable[ch] = ransomNoteTable[ch] + \
                1 if ransomNoteTable.get(ch) is not None else 1
        magazineTable = {}
        for ch in magazine:
            magazineTable[ch] = magazineTable[ch] + \
                1 if magazineTable.get(ch) is not None else 1

        for ch in ransomNoteTable:
            if magazineTable.get(ch) is None or magazineTable[ch] < ransomNoteTable[ch]:
                return False
        return True
        # Time: O(n), Space: O(1)


ransomNote = "a"
magazine = "b"
# Expected: False
result = Solution().canConstruct(ransomNote, magazine)
print(result)

ransomNote = "aa"
magazine = "ab"
# Expected: False
result = Solution().canConstruct(ransomNote, magazine)
print(result)

ransomNote = "aa"
magazine = "aab"
# Expected: False
result = Solution().canConstruct(ransomNote, magazine)
print(result)
