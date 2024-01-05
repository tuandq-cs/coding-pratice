class Solution:
    def hammingWeight(self, n: int) -> int:
        c = 0
        while(n):
            if n % 2 == 1:
                c += 1
            n = n >> 1
        return c
    # There is a most optimal solution: : Brian Kernighan's Algorithm
    # But I've not read this yet