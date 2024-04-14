from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        begin, end = 0, 0
        ans = 0
        n = len(fruits)
        freq = {}
        # expand the window
        while (end < n):
            # shink the window if invalid here
            while (len(freq) == 2 and fruits[end] not in freq):
                # update some state
                freq[fruits[begin]] -= 1
                if freq[fruits[begin]] == 0:
                    del freq[fruits[begin]]
                begin += 1
            # valid at [begin, end]
            freq[fruits[end]] = freq.get(fruits[end], 0) + 1
            ans = max(ans, end - begin + 1)
            end += 1
        return ans
    
fruits = [1,2,1]
#         ^
#              ^
# freq = {1: 2, 2: 1}
# ans = 3
out = Solution().totalFruit(fruits)
print(out)