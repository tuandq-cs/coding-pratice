# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(x, y):
    # write your code in Python
    i1, i2 = 0, 0
    while (i2 < len(y)):
        while i1 < len(x) and x[i1]!= y[i2]:
            i1 += 1
        if i1 == len(x):
            return False
        i1 += 1
        i2 += 1
    return True

x = "BCBAA"
y = "CBA"

out = solution(x, y)
print(out)