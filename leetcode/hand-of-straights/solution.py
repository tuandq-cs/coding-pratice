from heapq import heappop, heappush
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        counter = {}
        for num in hand:
            counter[num] = counter.get(num, 0) + 1
        minH = []
        for num in sorted(counter.keys()): # O(m*logm)
            heappush(minH, num)

        # O(m*logm), cuz every unique num will be pop out of the heap
        while (minH):
            # first element of group
            # [1st, 2nd, ...]
            fEle = heappop(minH)
            if counter[fEle] == 0:
                continue
            for j in range(1, groupSize):
                if counter.get(fEle+j, -1) < 0:
                    return False
                counter[fEle+j] -= counter[fEle]
                if counter[fEle+j] < 0:
                    return False
        return True
            
                    