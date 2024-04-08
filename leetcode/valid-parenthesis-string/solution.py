class Solution:
    def checkValidString(self, s: str) -> bool:
        balMin = 0
        balMax = 0
        for c in s:
            if c == '*':
                balMin -= 1
                balMax += 1
            if c == '(':
                balMin += 1
                balMax += 1
            if c == ')':
                balMin -= 1
                balMax -= 1
            if balMax < 0: return False
            balMin = max(balMin, 0)
        return balMin == 0
