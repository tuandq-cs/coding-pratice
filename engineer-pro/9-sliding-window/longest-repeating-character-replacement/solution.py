from curses.ascii import SO


class Solution:

    def numReplaceChars(self, begin: int, end: int, freq) -> int:
        if begin > end:
            return 0
        m = 0
        for c in freq:
            m = max(m, freq[c])
        return end - begin + 1 - m

    def characterReplacement(self, s: str, k: int) -> int:
        # empty window
        begin = 0
        end = -1
        freq = {}
        ans = 1
        while (begin < len(s)):
            # expand window
            while (end + 1 < len(s) and self.numReplaceChars(begin, end, freq) <= k):
                end += 1
                freq[s[end]] = freq.get(s[end], 0) + 1
            num = self.numReplaceChars(begin, end, freq)
            if end == len(s) - 1 and num <= k:
                # [begin, end]
                return max(ans, end - begin + 1)
            # [begin, end)
            ans = max(ans, end - begin)
            freq[s[begin]] -= 1
            begin += 1
        return ans




s = "ABAB"
#     ^
#       ^
# freq = {A: 2, B: 2}
k = 2

s = "AABABBA"
#        ^
#          ^
# freq = {A: 2, B: 2}
# ans = 4
k = 1

# edge
s = "ABCDEF"
k = 0 # -> out: 1

out = Solution().characterReplacement(s, k)
print(out)