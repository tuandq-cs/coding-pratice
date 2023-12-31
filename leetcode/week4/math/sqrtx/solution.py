class Solution:
    def mySqrt(self, x: int) -> int:
        # Find largest k**2 so that k**2 <= x, return k
        l = 0
        r = x
        k = 0
        while (l <= r):
            m = l + (r - l) // 2
            if m*m == x:
                return m
            if m*m > x:
                r = m - 1
            else:
                l = m + 1
                k = m
        return k
        # Time: O(log2(x))
    
x = 0
out = Solution().mySqrt(x)
print(out)