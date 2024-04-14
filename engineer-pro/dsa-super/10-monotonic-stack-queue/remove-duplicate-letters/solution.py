class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        freq = {}
        bitmask = 0
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        for c in s:
            iBit = (ord(c)-ord('a'))
            # pop out the stack
            while (len(stack) > 0 and stack[-1] >= c and freq[stack[-1]] > 0 and not (bitmask & (1 << iBit))):
                bitmask ^= 1 << (ord(stack[-1])-ord('a'))
                stack.pop()
            if not bitmask & (1 << iBit):
                # toggle 
                bitmask ^= 1 << iBit
                stack.append(c)
            freq[c] -= 1
        return ''.join(stack)
    

s = "bbcaac"
s = "edebbed"
out = Solution().removeDuplicateLetters(s)
print(out)