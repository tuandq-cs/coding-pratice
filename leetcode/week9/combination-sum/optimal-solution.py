from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def solve(i: int, curSum: int, comb: List[int]):
            if curSum > target or i == len(candidates):
                return
            if curSum == target:
                ans.append(comb)
                return
            solve(i, curSum+candidates[i], comb=comb+[candidates[i]])
            solve(i+1, curSum, comb)
        solve(0, 0, [])
        return ans
        # Time: 2^target
        # At each state, we have 2 decisions, and add at least 1 value to curSum (1+1+...=target)
        # So the height of tree at least = target
    
candidates = [2,3,6,7]
target = 7
# i = 1
# curSum = 3
# comb = [3, 3]
# ans = [[2, 2, 3],]
out = Solution().combinationSum(candidates, target)
print(out)

candidates = [2,3,5]
target = 8
out = Solution().combinationSum(candidates, target)
print(out)

candidates = [2]
target = 1
out = Solution().combinationSum(candidates, target)
print(out)