from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n0, n1 = 0, 0
        for i in students:
            if i == 1:
                n1 += 1
            if i == 0:
                n0 += 1
        i = 0
        while (i < len(sandwiches)):
            if sandwiches[i] == 0:
                if n0 == 0:
                    return n1
                n0 -= 1
            else:
                if n1 == 0:
                    return n0
                n1 -= 1
            i += 1
        return 0