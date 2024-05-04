from typing import List


def calcSum(mask: int, arr: List[int]) -> int:
    s = 0
    for i in range(len(arr)):
        # check bit
        if (mask >> i) & 1:
            s += arr[i]
    return s

def biSearch(arr: List[int], target: int) -> int:
    idx = -1
    l = 0
    r = len(arr) - 1
    while (l <= r):
        m = l + (r - l) // 2
        if arr[m] <= target:
            idx = m
            l = m + 1
        else:
            r = m - 1
    return idx


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) >> 1
        left = [[] for _ in range(n+1)]
        right = [[] for _ in range(n+1)]
        total = sum(nums)

        # generate all combinations
        for mask in range(1 << n): # O(2^n)
            # mask use for 2 halves
            numBits = mask.bit_count()
            lSum = calcSum(mask, nums[:n]) # O(n)
            left[numBits].append(lSum)
            rSum = calcSum(mask, nums[n:])
            right[numBits].append(rSum)
        # sort right part
        for i in range(n+1):
            right[i] = sorted(right[i])
        res = float('inf')
        for k in range(n+1): # O(n)
            # k bits from left, n-k bits from right
            r = right[n-k]
            for lSum in left[k]: # O(2^n)
                target = total // 2 - lSum
                # biSearch on r to find pos nearest target
                idx = biSearch(r, target)
                if idx == -1:
                    continue
                firstSum = lSum + r[idx]
                secondSum = total - firstSum
                res = min(res, abs(firstSum - secondSum))
        return res