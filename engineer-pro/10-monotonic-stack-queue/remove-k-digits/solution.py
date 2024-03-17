class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == len(num):
            return "0"
        monoStack = [] # increasing from bottom to top
        i = 0
        while (k > 0 and i < len(num)):
            # insert into the stack
            # pop out if the top of the stack > num[i] and make sure k > 0
            while (k > 0 and len(monoStack) > 0 and monoStack[-1] > num[i]):
                monoStack.pop()
                k -= 1
            monoStack.append(num[i])
            i += 1
        # case k > 0
        while (k > 0):
            monoStack.pop()
        # case k == 0
        while (i < len(num)):
            monoStack.append(num[i])
            i += 1
        res = ''
        flag = True
        for i in range(len(monoStack)):
            if flag == True and monoStack[i] == '0':
                continue
            if monoStack[i] != '0':
                flag = False
            res += monoStack[i]
        return res if res != '' else '0'
    
    # 953651629 k = 4