class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a, b = b, a
        s = []
        flag = False
        i = 0
        while (i < len(b)):
            v = ""
            if a[len(a)-1-i] == "0" and b[len(b)-1-i] == "0":
                v = "0" if not flag else "1"
                flag = False
            elif a[len(a)-1-i] == "1" and b[len(b)-1-i] == "1":
                v = "0" if not flag else "1"
                flag = True
            else:
                if not flag:
                    v = "1"
                    flag = False
                else:
                    v = "0"
            s.append(v)
            i += 1
        while (i < len(a)):
            if a[len(a)-1-i] == "0":
                s.append("0" if not flag else "1")
                flag = False
            else:
                s.append("1" if not flag else "0")
            i+=1
        if flag:
            s.append("1")
        out = ""
        while len(s) != 0:
            out += s.pop()
        return out
            
a = "11"
b = "1"
out = Solution().addBinary(a, b)
print(out)

a = "1010"
b = "1011"
out = Solution().addBinary(a, b)
print(out)

a = "100"
b = "110010"
out = Solution().addBinary(a, b)
print(out)
            