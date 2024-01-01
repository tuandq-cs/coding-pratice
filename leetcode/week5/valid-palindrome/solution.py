class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isValidChr(c: str) -> bool:
            return 'a' <= c <= 'z' or '0' <= c <= '9' or 'A' <= c <= 'Z'
        l = 0
        r = len(s) - 1
        while (l <= r):
            if not isValidChr(s[l]):
                l += 1
                continue
            if not isValidChr(s[r]):
                r -= 1
                continue
            lC = s[l]
            rC = s[r]
            if 'A' <= s[l] <= 'Z':
                lC = chr(ord(s[l])+32)
            if 'A' <= s[r] <= 'Z':
                rC = chr(ord(s[r])+32)
            if lC != rC:
                return False
            l += 1
            r -= 1
        return True
            
                 
    
s = "A man, a plan, a canal: Panama"
out = Solution().isPalindrome(s)
print(out)

s = "race a car"
out = Solution().isPalindrome(s)
print(out)

s = " "
out = Solution().isPalindrome(s)
print(out)