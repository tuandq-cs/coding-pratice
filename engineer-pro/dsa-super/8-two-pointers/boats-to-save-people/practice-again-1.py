from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        begin, end = 0, len(people) - 1
        boats = 0
        while (begin < end):
            if (people[begin] + people[end] > limit):
                end -= 1
            else:
                begin += 1
                end -= 1
            boats += 1
        return boats + 1 if begin == end else boats