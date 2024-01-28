from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        i = 0
        while (i < len(colors)):
            j = i + 1
            sumTime = neededTime[i]
            maxTime = neededTime[i]
            while(j < len(colors) and colors[i] == colors[j]):
                sumTime += neededTime[j]
                maxTime = max(maxTime, neededTime[j])
                j += 1
            ans += sumTime - maxTime
            i = j
        # Time: O(n)
        return ans

colors = "abaac"
neededTime = [1,2,3,4,5]
out = Solution().minCost(colors, neededTime)
print(out)

colors = "abc"
neededTime = [1,2,3]
out = Solution().minCost(colors, neededTime)
print(out)

colors = "aabaa"
neededTime = [1,2,3,4,1]
out = Solution().minCost(colors, neededTime)
print(out)