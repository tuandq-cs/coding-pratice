from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for t in tokens:
            if t not in ('+','-','/','*'):
                s.append(int(t))
                continue
            num2, num1 = s.pop(), s.pop()
            newNum = 0
            if t == '+':
                newNum = num1 + num2
            elif t == '-':
                newNum = num1 - num2
            elif t == '*':
                newNum = num1 * num2
            else:
                newNum = int(num1 / num2)
            s.append(newNum)
        return s[0]
    
tokens = ["2","1","+","3","*"]
out = Solution().evalRPN(tokens)
print(out)

tokens = ["4","13","5","/","+"]
out = Solution().evalRPN(tokens)
print(out)

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
out = Solution().evalRPN(tokens)
print(out)