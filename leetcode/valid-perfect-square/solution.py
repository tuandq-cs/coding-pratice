class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r  = 0, num
        while (l <= r):
            m = l + (r - l) // 2
            if m * m == num:
                return True
            if m * m < num:
                l = m + 1
            else:
                r = m - 1
        return False