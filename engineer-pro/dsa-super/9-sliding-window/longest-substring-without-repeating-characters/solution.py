class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        # Empty window
        begin = 0
        end = 0
        
        freq = {}
        ans = 0
        while (end < len(s)):
            # while the window should be expanded
            # [begin, end)
            while (end < len(s) and freq.get(s[end], 0) == 0):
                if freq.get(s[end]) is None:
                    freq[s[end]] = 0    
                freq[s[end]] = freq.get(s[end], 0) + 1
                end += 1
            ans = max(ans, end - begin)
            freq[s[begin]] -= 1
            begin += 1
        return ans
    

s = " "
s = "abcabcbb"
out = Solution().lengthOfLongestSubstring(s)
print(out)