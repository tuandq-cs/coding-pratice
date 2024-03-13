from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums)
        if s % k != 0:
            return False
        visited = [False] * len(nums)
        targetSum = s // k
        n = len(nums)
        nums = sorted(nums, reverse=True)
        def recur(i: int, curSum: int, numPar: int):
            if numPar == 1:
                return True

            if curSum == targetSum:
                return recur(0, 0, numPar-1)
            for j in range(i, n):
                if j > 0 and not visited[j-1] and nums[j] == nums[j-1]:
                    continue
                if visited[j] or curSum + nums[j] > targetSum:
                    continue
                visited[j] = True
                if recur(j+1, curSum+nums[j], numPar):
                    return True
                visited[j] = False
            return False
        return recur(0, 0, k)
                
    
nums = [2,9,4,7,3,2,10,5,3,6,6,2,7,5,2,4]
k = 7
out = Solution().canPartitionKSubsets(nums, k)
print(out)