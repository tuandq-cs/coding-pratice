class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance = 0
        numInserts = 0
        for c in s:
            if c == '(':
                balance += 1
            else:
                balance -= 1
            if (balance < 0):
                numInserts += 1
                balance = 0
        return numInserts + balance