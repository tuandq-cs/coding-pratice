from typing import List


class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        x = 0
        for i in range(len(arr2)):
            x ^= arr2[i]
        res = 0
        for i in range(len(arr1)):
            res ^= (arr1[i] & x)
        return res
        # Time: O(n+m), Space: O(1)
        # n: length of arr1, m: length of arr2


# non-negative
# 1 <= arr1.length, arr2.length <= 10^5
# 0 <= arr1[i], arr2[j] <= 10^9
arr1 = [1, 2, 3, 7, 10]
arr2 = [6, 5, 11, 13, 15, 20]
out = Solution().getXORSum(arr1, arr2)
print(out)
# find all pairs (i, j) => length: O(m*n)
# (item[i] & item[j1]) ^ (item[i] & item[j2]) ^ (item[i] & item[j3])
arr1 = [1, 2, 3]
arr2 = [6, 5]
out = Solution().getXORSum(arr1, arr2)
print(out)
# pairs = [(1, 6), (1, 5)]
# pairs = []
# (1 & 6) ^ (1 & 5) => 1 & (6 ^ 5)
# (1 & 6) ^ (1 & 5) ^ (2 & 6) ^ (2 & 5) =>  (1 & (6 ^ 5)) ^ (2 & (6 ^ 5))


arr1 = [12]
arr2 = [4]
out = Solution().getXORSum(arr1, arr2)
print(out)
