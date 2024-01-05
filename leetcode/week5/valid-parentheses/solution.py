class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        m = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        for c in s:
            if c in ('{', '[', '('):
                stack.append(c)
            else:
                if len(stack) == 0:
                    # Break constraint 3
                    return False
                if m[stack.pop()] != c:
                    # Constaint 2
                    return False   
        return len(stack) == 0 # Constraint 1
    

s = "()"
out = Solution().isValid(s)
print(out)

s = "()[]{}"
out = Solution().isValid(s)
print(out)

s = "(]"
out = Solution().isValid(s)
print(out)