from typing import List


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        if len(b) == 0:
            return 1
        k = self.divTwo(b)
        subPow = self.superPow(a, k)
        return (subPow*subPow*(a%1337)) % 1337 if b[-1] & 1 else (subPow*subPow) % 1337
    
    def divTwo(self, b: List[int]) -> List[int]:
        ans = []
        residual = 0
        for i, num in enumerate(b):
            m = residual * 10 + num
            residual = m % 2
            if (m // 2 == 0 and i == 0):
                continue
            ans.append(m // 2)
        return ans
    
a = 2
b = [3]
# b = [3], k = [1], subPow = 2, ans = 2*2*2
# b = [1], k = [], subPow = 1, ans = 1*1*2 = 2

a = 2
b = [1,0]
# b = [1, 0], k = [5], subPow = ?
# b = [5], k = [2], subPow = ?
# b = [2], k = [1], subPow = ?

a = 1
b = [4,3,3,8,5,2]

out = Solution().superPow(a, b)
print(out)
