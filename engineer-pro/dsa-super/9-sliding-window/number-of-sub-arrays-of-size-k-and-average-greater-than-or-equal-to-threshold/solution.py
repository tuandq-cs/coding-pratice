from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # [begin, end]
        n = len(arr)
        begin = 0
        end = 0
        cnt = 0
        s = 0
        while (end < n):
            # expand window
            while (end < n and end - begin + 1 <= k):
                s += arr[end]
                end += 1
            # condition satisfied
            if end - begin == k and s >= threshold*k:
                cnt += 1
            s -= arr[begin]
            begin += 1
        return cnt