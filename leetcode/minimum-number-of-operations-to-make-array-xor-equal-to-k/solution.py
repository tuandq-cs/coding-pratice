from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # 0001000
        # 0101010
        # 1010100

        # 0101010

        # at bit i, cnt0 is count 0 bits, cnt1 is count 1 bits
        # 0 ^ 1 or 1 ^ 0 = 1, cnt1 even => curXOR = 0, cnt1 odd => curXOR = 1
        # if i bit of k = 1, curXOR at i = 0 ^ (cnt1 % 2) => ops += 1 if curXOR != i bit of k
        # 2 ^ 20  ~ 2^10 * 2^10 > 10^6
        ops = 0
        for i in range(20):
            cnt1 = 0
            for num in nums:
                # check bit at i
                cnt1 += (num >> i) & 1
            curXOR = 0 ^ (cnt1 % 2)
            if curXOR != ((k >> i) & 1):
                ops += 1
        # Time: 20*O(n), n is length of nums, 20 is bits represent for nums[i]
        return ops

