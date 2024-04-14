from typing import List

def checkBit(mask: int, i: int):
    return (mask >> i) & 1 == 1

class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        m = len(requests)
        def checkPossible(mask: int):
            cnt = [0 for _ in range(n)]
            for i in range(m):
                if checkBit(mask, i):
                    f, t = requests[i]
                    cnt[f] -= 1
                    cnt[t] += 1
            for v in cnt:
                if v != 0:
                    return False
            return True

        # generate state
        maxReq = 0
        for mask in range(1, 1 << m): # O(2^m)
            if mask.bit_count() <= maxReq:
                continue
            if checkPossible(mask): # O(m)
                maxReq = mask.bit_count()
        return maxReq
        # Time: O(2^m * m)

n = 5
requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]
out = Solution().maximumRequests(n, requests)
print(out)

n = 3
requests = [[0,0],[1,2],[2,1]]
out = Solution().maximumRequests(n, requests)
print(out)

n = 4
requests = [[0,3],[3,1],[1,2],[2,0]]
out = Solution().maximumRequests(n, requests)
print(out)