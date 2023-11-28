from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.recur(n, k, 1, [], res)
        return res

    def recur(self, n, k, start, comb, res):
        # n = 4
        # k = 2
        # start = 5
        # comb = [1]
        # res = [[1, 2], [1, 3], [1, 4]]
        if len(comb) == k:
            res.append(comb.copy())
            return

        # 1 -> 4
        for i in range(start, n + 1):
            # i = 2
            comb.append(i)
            self.recur(n, k, i+1, comb, res)
            comb.pop()


n = 4
k = 2
result = Solution().combine(n, k)
print(result)

#   1           2
# 2   3  4
#
