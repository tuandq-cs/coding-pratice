class Solution:
    def isPalindrome(self, s: str) -> bool:
        return self.secondSolution(s)

    def secondSolution(self, s: str) -> bool:
        def is_valid_char(c):
            return ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9')
        l = 0
        r = len(s) - 1 - l
        while (l <= r):
            if not is_valid_char(s[l]):
                l += 1
                continue
            if not is_valid_char(s[r]):
                r -= 1
                continue
            c_l = chr(ord(s[l]) + 32) if 'A' <= s[l] <= 'Z' else s[l]
            c_r = chr(ord(s[r]) + 32) if 'A' <= s[r] <= 'Z' else s[r]
            if c_l != c_r:
                return False
            l += 1
            r -= 1
        return True

    def firstSolution(self, s: str) -> bool:
        # 1. Process the phrase to a string
        new_s = ""
        for c in s:
            # lowercase letters & numbers
            if (48 <= ord(c) and ord(c) <= 57) or (97 <= ord(c) and ord(c) <= 122):
                new_s += c
            # uppercase letters
            if 65 <= ord(c) and ord(c) <= 90:
                new_s += chr(ord(c) + 32)
        # Time: O(n), Space: O(n)
        # 2. Check whether the string is palindrome
        for l in range(len(new_s) // 2):
            r = len(new_s) - 1 - l
            if r < l:
                break
            if new_s[l] != new_s[r]:
                return False
        # Time: O(n/2), Space: O(1)

        # Overall: O(n), Space: O(n)
        return True


# General cases
s = "A man, a plan, a canal: Panama"
# Expected: True
result = Solution().isPalindrome(s)
print(result)

s = "race a car"
# Expected: False
result = Solution().isPalindrome(s)
print(result)

s = "rac a car"
# Expected: True
result = Solution().isPalindrome(s)
print(result)

# Corner cases
# s is empty
s = " "
result = Solution().isPalindrome(s)
print(result)
