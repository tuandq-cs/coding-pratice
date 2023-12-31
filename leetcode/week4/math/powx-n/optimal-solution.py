# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         if x == 0:
#             return 0
#         if n < 0:
#             return 1 / self.myPow(x, -n)
#         if n == 0:
#             return 1
#         ans = self.myPow(x, n // 2)
#         ans *= ans
#         if n % 2 == 1:
#             ans *= x
#         return ans
#         # Time: O(log2(n)), Space: O(log2(n)) because of recursion call

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n < 0:
            return 1 / self.myPow(x, -n)
        mul = 1
        while (n):
            if (n & 1 != 0):
                mul *= x
            x *= x
            n = n >> 1
        return mul
        # Time: O(log2(n)), Sapce: O(1)
    
x = 0.00001
n = 2147483647
out = Solution().myPow(x, n)
print(out)