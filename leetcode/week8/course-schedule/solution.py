from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def takeCourse(i: int):
            if states[i] == 2:
                return True
            if states[i] == 1:
                return False
            states[i] = 1
            for preNode in nodes[i]:
                if not takeCourse(preNode):
                    return False
            states[i] = 2
            return True
        
        nodes = [[] for _ in range(numCourses)]
        # Time: O(p), p: length of prerequisites <= 7000
        for item in prerequisites:
            nodes[item[0]].append(item[1])
        states = [0] * numCourses
        # 0: not processed
        # 1: processing
        # 2: processed
        for i in range(numCourses):
            if not takeCourse(i):
                return False
        return True

numCourses = 2
prerequisites = [[1,0]]

# nodes = [[], [0]]
# states = [2, 2]
out = Solution().canFinish(numCourses, prerequisites)
print(out)

numCourses = 2
prerequisites = [[1,0],[0,1]]
# nodes = [[1], [0]]
# states = [1, 1]
out = Solution().canFinish(numCourses, prerequisites)
print(out)

numCourses = 5
prerequisites = [[1,2], [2, 3], [2, 4], [4, 2]]
# nodes = [[], [2], [3, 4], [], [2]]
# states = [2, 1, 1, 2, 1]
out = Solution().canFinish(numCourses, prerequisites)
print(out)
