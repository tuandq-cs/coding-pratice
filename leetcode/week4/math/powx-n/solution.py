class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n < 0:
            return 1 / self.myPow(x, -n)
        if x < 0 and n % 2 != 0:
            return -self.myPow(-x, n)
        if n == 0:
            return 1
        h = 1
        mul = x
        while (h < n):
            mul *= mul
            h += h
        return mul * self.myPow(x, n-h)
    
x = 0.00001
n = 2147483647
out = Solution().myPow(x, n)
print(out)