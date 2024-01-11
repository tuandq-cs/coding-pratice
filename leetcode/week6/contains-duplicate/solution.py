from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        m = {}
        for num in nums:
            if m.get(num) is None:
                m[num] = 0
            m[num] += 1
        for num in m:
            if m[num] >= 2:
                return True
        return False