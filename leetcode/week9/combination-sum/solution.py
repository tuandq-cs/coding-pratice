from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        memo = {}
        mIndex = {}
        for i, can in enumerate(candidates):
            mIndex[can] = i

        def solve(target: int):
            if target < 0:
                return []
            if target == 0:
                return [[0 for _ in range(len(candidates))]]
            if memo.get(target) is not None:
                return memo[target]
            counters = []
            for can in candidates:
                subCounters = solve(target - can)
                if len(subCounters) == 0:
                    continue
                for subCounter in subCounters:
                    newCounter = subCounter.copy()
                    newCounter[mIndex[can]] += 1
                    counters.append(newCounter)
            memo[target] = counters
            return counters
        counters = solve(target)
        mComb = {}
        for counter in counters:
            hashKey = ",".join(
                [f"{can}:{counter[i]}" for i, can in enumerate(candidates)])
            comb = []
            for i, can in enumerate(candidates):
                comb.extend([can]*counter[i])
            mComb[hashKey] = comb
        return list(mComb.values())


candidates = [2, 3, 6, 7]
target = 7
out = Solution().combinationSum(candidates, target)
print(out)

candidates = [2, 3, 5]
target = 8
out = Solution().combinationSum(candidates, target)
print(out)
