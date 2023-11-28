from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        perms = self.perm(n, {})
        m_char = [""] * (n + 1)
        for i in range(1, n+1):
            m_char[i] = f"({m_char[i-1]})"
        result = []
        for p in perms:
            result.append("".join(m_char[i] for i in p))
        return result

    def perm(self, n: int, memo: dict):
        if memo.get(n):
            return memo[n]
        if n == 1:
            return [[1]]
        permutations = [[n]]
        for i in range(1, n):
            i_permutations = self.perm(i, memo)
            memo[i] = i_permutations
            for i_perm in i_permutations:
                permutations.append(i_perm + [n - i])
        return permutations

# General case
# n = 8
# memo = {
#   1: [[1]]
#   2: [[2], [1, 1]]
#   3: [[1], [1, 2], [2, 1], [1, 1, 1]]
# }
# permutations = [[8], [1, 7], [2, 6], [1, 1, 6], [1, 5], [1, 2, 5], [2, 1, 5], [1, 1, 1, 5]]
# i = 3
# stack = []
# i_permuations = [[1, 5], [1, 2, 5], [2, 1, 5], [1, 1, 1, 5]]


# n = 3
# permutations = [[3]]
# i = 3
# i_permutations = [[1], [1, 2], [2, 1], [1, 1, 1]]
result = Solution().generateParenthesis(n=3)
print(result)


# Corner case
# n = 1
