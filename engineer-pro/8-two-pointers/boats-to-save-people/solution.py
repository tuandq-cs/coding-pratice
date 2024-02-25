from typing import List


class Solution:
    def bSearch(self, people: List[int], p1: int, p2: int, limit: int) -> int:
        l = p1 + 1
        r = p2
        i = -1
        while (l <= r):
            m = l + (r - l) // 2
            if people[p1] + people[m] <= limit:
                l = m + 1
                i = m
            else:
                r = m - 1
        return i
            
            
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        p1 = 0
        p2 = len(people) - 1
        boats = 0
        while (p1 < p2):
            i = self.bSearch(people, p1, p2, limit)
            if i == -1:
                boats += (p2 - p1 + 1)
                return boats
            boats += (p2 - i + 1)
            p2 = i - 1
            p1 += 1
        if p1 == p2:
            return boats + 1
        return boats
    
people = [1,2]
limit = 3

people = [3,2,2,1]
limit = 3

people = [3,5,3,4]
limit = 5

people = [445,597,385,576,291,190,187,613,657,477]
limit = 1000

people = [8,2,3,6,2,6]
limit = 8

# people = [2, 2, 3, 6, 6, 8]
#           ^
#                          ^
out = Solution().numRescueBoats(people, limit)
print(out)

