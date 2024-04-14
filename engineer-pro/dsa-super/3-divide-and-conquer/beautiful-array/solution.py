from typing import List


class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        if n == 1:
            return [1]
        subArr = self.beautifulArray(n-1)
        odd = [2*v-1 for v in subArr]
        even = [2*v for v in subArr]
        return [v for v in odd + even if v <= n]


n = 4
n = 5
out = Solution().beautifulArray(n)
print(out)
