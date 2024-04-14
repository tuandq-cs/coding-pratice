from typing import List


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        freq = {}
        ans = 0
        m = 0
        for p in piles:
            if p > m:
                m = p
            if freq.get(p) is None:
                freq[p] = 0
            freq[p] += 1
            ans += p
        for numStones in range(m, 1, -1):
            if freq.get(numStones) is None:
                continue
            canTake = min(k, freq[numStones])
            ans -= canTake * (numStones // 2)
            remainStones = numStones - numStones // 2
            if freq.get(remainStones) is None:
                freq[remainStones] = 0
            freq[remainStones] += canTake
            freq[numStones] -= canTake
            k -= canTake
            if k == 0:
                break
        return ans
        # Time: O(max(piles)), Space: O(n)

piles = [5,4,9]
k = 2
# freq = { 5: 1, 4: 1, 9: 1, 3: 1}
# k = 0
# ans = 12
# numStones = 5, canTake = 1, remainStones = 3

piles = [4,3,6,7]
k = 3
out = Solution().minStoneSum(piles, k)
print(out)