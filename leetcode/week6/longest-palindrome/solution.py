class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = {}
        for c in s:
            if counter.get(c) is None:
                counter[c] = 0
            counter[c] += 1
        result = 0
        flag = False
        for c in counter:
            l = (counter[c] // 2) * 2
            result += l
            if counter[c] - l == 1:
                flag = True
        return result + 1 if flag else result
    
s = "aAbccccdd"
out = Solution().longestPalindrome(s)
print(out)

s = "a"
out = Solution().longestPalindrome(s)
print(out)


