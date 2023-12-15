class Solution:
    def isValid(self, s: str) -> bool:
        m = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []
        for c in s:
            if c in ('(', '{', '['):
                stack.append(c)
            else:
                # Constraint 2
                if len(stack) == 0:
                    return False
                # Constraint 3
                if m[c] != stack.pop():
                    return False
        return len(stack) == 0  # Constraint 1


s = '{(())}[]'  # expected: valid
# stacks = []
print(Solution().isValid(s))

s = '{(())}['  # expected: invalid
# stacks = [[], violate constraint 1
print(Solution().isValid(s))


s = '{(())}]'  # expected: invalid
# stacks = [], c = ], violate constraint 2
print(Solution().isValid(s))

s = '({)}'  # expected: invalid
# stacks = [({], c = ), m[c] = (, violate constraint 3
print(Solution().isValid(s))
