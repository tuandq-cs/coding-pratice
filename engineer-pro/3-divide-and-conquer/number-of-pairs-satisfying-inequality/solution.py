from typing import List


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        # nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff
        # nums1[i] - nums2[i] <= nums2[j] - nums2[j] + diff

        def countPairs(l: int, r: int):
            if not l < r:
                return 0
            m = l + (r - l) // 2
            cnt = 0
            cnt += countPairs(l, m)
            cnt += countPairs(m+1, r)
            # sort copy arr from right part
            rightPart = []
            for i in range(m+1, r+1):
                rightPart.append(nums1[i]-nums2[i])
            rightPart = sorted(rightPart)
            # each item from left part
            for i in range(l, m+1):
                index = bSearch(rightPart, nums1[i]-nums2[i]-diff)
                if index == -1:
                    continue
                cnt += (r - (m+1+index) + 1)
            # Time: O(n*log(n)), Space = O(n*log(n))
            return cnt

        def bSearch(arr: List[int], target: int):
            l = 0
            r = len(arr) - 1
            index = -1
            while (l <= r):
                m = l + (r - l) // 2
                if arr[m] >= target:
                    index = m
                    r = m - 1
                else:
                    l = m + 1
            return index
        
        return countPairs(0, len(nums1) - 1)
        
nums1 = [3,2,5]
nums2 = [2,2,1]
diff = 1
# l = 0, r = 2, m = 1
    # l = 0, r = 1, m = 0
        # cnt = 0
        # l = 0, r = 0, cnt += 0
        # l = 1, r = 1, cnt += 0
        # rightPart = [0]
        # i = 0, target = 1 - 1 = 0
        # index = 0
        # cnt += (1 - (0+1+0) + 1) = 1
    # l = 2, r = 2, cnt += 0
# rightPart = [4]
# i = [0, 2)
# i = 0, target = 3 - 2 - 1 = 0
# index = 0, cnt += (2 - (1+1+0) + 1) = 1
# i = 1, target = 2 -2 - 1 = -1
# index = 0, cnt += (2 - (1+1+0) + 1) = 1

nums1 = [3,-1]
nums2 = [-2,2]
diff = -1

out = Solution().numberOfPairs(nums1, nums2, diff)
print(out)

        
