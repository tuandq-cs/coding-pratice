
# https://leetcode.com/problems/multiply-strings/

# num1 = "1234"
# num2 = "456"

# r1 = "1234" * "4" = abc00 
# r2 = "1234" * "5" = xyz0
# r3 = "1234" * "6" = mnj

# r = r1 + r2 + r3 = ""

def multiply(num1: str, num2: str) -> str:
    num1, num2 = (num2, num1) if len(num2) > len(num1) else (num1, num2)
    # "123", "45"
    r = [] # len(num2)
    nOfZero = 0
    for i in range(len(num2)-1, -1, -1):
        x = multiply_with_one(num1, int(num2[i])) 
        # "123", 5 -> "615"
        # "123", 4 -> "492"
        x = f'{x}{"".join(["0" for x in range(nOfZero)])}' 
        # "615"
        # "4920"
        r.append(x)
        # r = ["615"]
        # r = ["615", "4920"]
        nOfZero += 1
    # O(t1) = n * n
    result = "0"
    for x in r:
        result = add(result, x)
        # "0", "615" -> "615"
        # "615", "4920"
    # O(t2) = n * n
    return result

def multiply_with_one(num1: str, num2: int) -> str:
    # num1, num2 = "123", 5
    s = []
    r = 0
    for i in range(len(num1)-1, -1, -1):
        # i = 0
        # i = 1
        # i = 2
        x = num2 * int(num1[i]) 
        # x = 5 * 3
        # x = 5 * 2
        # x = 5 * 1
        x = x + r 
        # x = 15 + 0
        # x = 10 + 1
        # x = 5 + 1
        s.append(x % 10) 
        # s = [5]
        # s = [5, 1]
        # s = [5, 1, 6]
        r = x // 10 
        # r = 1
        # r = 1
    if r != 0:
        s.append(r)
    return get_str_from_stack(s)

# "0", "615"
# "615", "4920"
def add(num1: str, num2: str) -> str:
    num1, num2 = (num2, num1) if len(num2) > len(num1) else (num1, num2)
    # "615", "0"
    # "4920", "615"
    r = 0
    s = []
    iOfNum2 = len(num2) - 1
    for i in range(len(num1)-1, -1, -1):
        # i = 0
        # i = 1
        # i = 2
        # i = 3
        n1, n2 = (int(num1[i]), int(num2[iOfNum2])) if iOfNum2 >= 0 else (int(num1[i]), 0)
        # 0, 5
        # 2, 1
        # 9, 6
        # 4, 0
        x = n1 + n2 + r
        # x = 0 + 5 + 0
        # x = 2 + 1 + 0
        # x = 9 + 6 + 0
        # x = 4 + 0 + 1
        s.append(x % 10)
        # s = [5]
        # s = [5, 3]
        # s = [5, 3, 5]
        # s = [5, 3, 5, 5]
        r = x // 10
        # r = 0
        # r = 0
        # r = 1
        # r = 0
        iOfNum2 -= 1
    if r != 0:
        s.append(r)
    return get_str_from_stack(s)

def get_str_from_stack(s):
    result = ""
    is_all_zero = True
    for i in range(len(s)-1, -1, -1):
        if is_all_zero:
            is_all_zero = s[i] == 0
        if not is_all_zero:
            result += f'{s[i]}'
    return "0" if is_all_zero else result

num1 = "45" 
num2 = "123"
r = multiply(num1, num2)
print(r)

        
        

