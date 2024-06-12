from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        curXOR = k
        for num in nums:
            curXOR ^= num
        return curXOR.bit_count()

