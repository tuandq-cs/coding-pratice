from math import floor, sqrt
from typing import List


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        maxNum = max(nums)
        setNum = set()
        res = -1
        for num in nums:
            setNum.add(num)
            cnt = 1
            # square
            tmp = num
            while tmp <= maxNum:
                tmp *= tmp
                if tmp not in setNum:
                    break
                cnt += 1
            # sqrt
            tmp = num
            while tmp != 1:
                tmp = sqrt(tmp)
                if tmp != floor(tmp) or tmp not in setNum:
                    break
                cnt += 1
            if cnt >= 2:
                res = max(res, cnt)
        return res