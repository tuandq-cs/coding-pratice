class Solution:
    def findLongestLocal(self, l, r: int, s: str):
        # Time: O(N)
        sub_s = ""
        while (l >= 0 and r < len(s)):
            if s[l] != s[r]:
                return sub_s
            sub_s = s[l] if l == r else s[l] + sub_s + s[r]
            l -= 1
            r += 1
        return sub_s

    def longestPalindrome(self, s: str) -> str:
        global_longest = ""
        for i, c in enumerate(s):
            local_1 = self.findLongestLocal(i, i, s)
            local_2 = self.findLongestLocal(i, i+1, s)
            local_longest = local_1 if len(local_1) > len(local_2) else local_2
            if len(local_longest) > len(global_longest):
                global_longest = local_longest
        # Time: O(n^2), Space: O(n), n is length of s
        return global_longest


# General cases
s = "babad"
# i = 2
# global_longest = "bab"
# l = 0, r = 4, sub_s = "aba"
# local_1 = "bab"
# local_2 = "abc"
# local_longest = "aba"
result = Solution().longestPalindrome(s)
print(result)

# Corner cases
# s with only one char
s = "s"
# Expected: "s"
# global_longest = "s"
# i = 0
# l = 0, r = 1, sub_s = "s"
# local_1 = "s"
# local_2 = ""
# local_longest = "s"
result = Solution().longestPalindrome(s)
print(result)

# s with duplicate chars
s = "bbb"
# Expected: "bbb"

# global_longest = "bbb"
# i = 2
# l = 2, r = 3, sub_s = ""
# local_1 = "b"
# local_2 = ""
# local_longest = "b"
result = Solution().longestPalindrome(s)
print(result)
