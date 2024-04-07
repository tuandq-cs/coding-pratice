from typing import List


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.subProblem(nums, k) - self.subProblem(nums, k - 1)


    def subProblem(self, nums: List[int], k: int) -> int:
        # 1 <= nums[i], k <= nums.length
        n = len(nums)
        # init window
        begin = 0
        end = -1
        freq = {}
        cnt = 0
        # expand window
        while (end + 1 < n):
            end += 1
            freq[nums[end]] = freq.get(nums[end], 0) + 1
            # shink the window
            while (begin <= end and len(freq) > k):
                freq[nums[begin]] -= 1
                if freq[nums[begin]] == 0:
                    del freq[nums[begin]]
                begin += 1
            # len(freq) <= k
            cnt += (end - begin + 1)
        return cnt

nums = [1,2,1,2,3]
k = 2
out = Solution().subarraysWithKDistinct(nums, k)
print(out)