class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        balance = 0
        l = []
        for c in s:
            if c == '(':
                balance += 1
            if c == ')':
                balance -= 1
            if balance < 0:
                balance = 0
            else:
                l.append(c)
        i = len(l) - 1
        while balance > 0:
            if l[i] == '(':
                l[i] = ''
                balance -= 1
            i -= 1
        return ''.join(l)