class Solution:
    def checkSign(self, part: str) -> bool:
        # pointer i will start at 1 if part[0] in ('+', '-')
        i = 1 if part[0] in ('+', '-') else 0
        # case only '.'
        if i == 1 and i == len(part):
            return False
        # only has +,- at first element
        while (i < len(part)):
            if part[i] in ('+', '-'):
                    return False
            i += 1
        return True

    def isDecimal(self, part: str) -> bool:
        if len(part) == 0:
            return False
        if self.checkSign(part) is False:
            return False
        start = 1 if part[0] in ('+', '-') else 0
        firstPart, secondPart = '', ''
        for i in range(start, len(part)):
            if part[i] == '.':
                secondPart = part[i+1:]
                break
            firstPart += part[i]
        return len(firstPart) != 0 or len(secondPart) != 0


    def isInteger(self, part: str) -> bool:
        if len(part) == 0:
            return False
        if self.checkSign(part) is False:
            return False
        for i in range(len(part)):
            if part[i] == '.':
                return False
        return True


    def isNumber(self, s: str) -> bool:
        # decimal | integer [e|E integer]
        # decimal: [-+][0-9]*.[0-9]+ | [0-9]+.[0-9]*
        # integer: [-+][0-9]+
        numDots = 0
        numE = 0
        for c in s:
            if not ('0' <= c <= '9' or c in ('e','E', '+', '-', '.')):
                return False
            if c == 'e' or c == 'E':
                numE += 1
            if c == '.':
                numDots += 1
        # check if there are more than 1 dot or 1e|E
        if numDots > 1 or numE > 1:
            return False
        
        firstPart = ''
        hasDot = False
        hasE = False
        secondPart = ''
        for i, c in enumerate(s):
            if c == '.':
                hasDot = True
            if c == 'e' or c == 'E':
                hasE = True
                secondPart = s[i+1:]
                break
            firstPart += c
        if hasDot:
            if self.isDecimal(firstPart) is False:
                return False
        else:
            if self.isInteger(firstPart) is False:
                return False
        if hasE:
            if self.isInteger(secondPart) is False:
                return False
        return True
    
s = "3."
out = Solution().isNumber(s)
print(out)
