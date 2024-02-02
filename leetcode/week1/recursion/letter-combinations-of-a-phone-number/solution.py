from typing import List


mDigits = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        self.recur(0, digits, "", res)
        return res

    def recur(self, i: int, digits: str, cur_repr: str, comb: List[str]):
        if len(digits) == 0:
            return []
        if len(cur_repr) == len(digits):
            comb.append(cur_repr)
            return
        d = digits[i]
        for c in mDigits[d]:
            self.recur(i+1, digits, cur_repr + c, comb)


# General case
digits = "23"
# expected []
result = Solution().letterCombinations(digits)
print(result)

# Corner case
# digits.length = 0 or 1
digits = ""
# expected []
result = Solution().letterCombinations(digits)
print(result)

digits = "2"
# expected = ["a", "b", "c"]
result = Solution().letterCombinations(digits)
print(result)
