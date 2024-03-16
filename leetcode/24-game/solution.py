from typing import List


class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        return self.recur([num*1.0 for num in cards])
        
    def recur(self, cards: List[float]) -> bool:
        if len(cards) == 1:
            return abs(cards[0] - 24.0) < 0.01
        for i in range(len(cards)-1):
            for j in range(i+1, len(cards)):
                newCards = []
                for k in range(len(cards)):
                    if k == i or k == j:
                        continue
                    newCards.append(cards[k])
                p1, p2 = cards[i], cards[j]
                cases = [p1+p2,abs(p1-p2), p1*p2]
                if abs(p1 - 0.0) > 0.01:
                    cases.append(p2/p1)
                if abs(p2 - 0.0) > 0.01:
                    cases.append(p1/p2)
                for num in cases:
                    newCards.append(num)
                    if self.recur(newCards):
                        return True
                    newCards.pop()
        return False
        # Time: O(n^2 * 4^n)
