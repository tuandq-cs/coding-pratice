class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map_pos = {}
        left_pointer = 0
        global_max = 0
        for i, c in enumerate(s):
            if map_pos.get(c) is not None and left_pointer <= map_pos[c]:
                left_pointer = map_pos[c] + 1
            map_pos[c] = i
            global_max = max(global_max, i - left_pointer + 1)
        # Time: O(n), Space: O(1)
        return global_max


# General cases
s = "acbdcbafb"
# Expected: length of "dcbaf": 5
result = Solution().lengthOfLongestSubstring(s)
print(result)

s = "pwwkew"
# Expcted: length of "wke" or "kew": 3
result = Solution().lengthOfLongestSubstring(s)
print(result)

# Corner cases
# s is empty
s = ""
# Expected: 0
result = Solution().lengthOfLongestSubstring(s)
print(result)

# s with repeated items
s = "bbb"
# Expected: 1

result = Solution().lengthOfLongestSubstring(s)
print(result)
