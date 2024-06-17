from math import ceil


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = ceil(c ** 0.5)
        while (a <= b):
            if a**2 + b**2 == c:
                return True
            if a**2 + b**2 > c:
                b -= 1
            else:
                a += 1
        # Time: O(c^1/2), c^1/2 ~ 10^9/2 ~ 10^5
        return False