from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m1 = set()
        for num in nums1:
            m1.add(num)
        res = set()
        for num in nums2:
            if num in res:
                continue
            if num in m1:
                res.add(num)
        return list(res)