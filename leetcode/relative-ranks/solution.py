from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        score = [(score[i], i) for i in range(n)]
        score = sorted(score, reverse=True)
        res = ["" for i in range(n)]
        tmp = ["Gold Medal","Silver Medal","Bronze Medal"]
        for i in range(n):
            s, idx = score[i]
            if i < 3:
                res[idx] = tmp[i]
            else:
                res[idx] = f'{i+1}'
        return res