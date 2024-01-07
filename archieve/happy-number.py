# https://leetcode.com/problems/happy-number/
# This problem can be solve by using the Floyd Cycle Detection

def get_map_digits(n: int) -> dict:
    m = {}
    while n != 0:
        tmp = n % 10
        m[tmp] = m.get(tmp) + 1 if m.get(tmp) else 1
        n = n // 10
    return m

def process(n: int) -> int:
    m = get_map_digits(n)
    r = 0
    for k in m:
        r += m[k] * k ** 2
    return r

def isHappy(n: int) -> bool:
    m = {}
    new_value = n
    while m.get(new_value) == None:
        if new_value == 1:
            return True
        m[new_value] = True
        new_value = process(new_value)
    return False

n = 11
print(isHappy(n))
    



        