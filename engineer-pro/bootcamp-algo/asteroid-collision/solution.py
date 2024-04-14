from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        stack = []
        for i in range(n):
            if asteroids[i] >= 0:
                stack.append(asteroids[i])
            else:
                # pop until the current item is destroyed
                destroyed = False
                while len(stack) > 0 and stack[-1] > 0 and not destroyed:
                    if -asteroids[i] < stack[-1]:
                        destroyed = True
                    else:
                        if -asteroids[i] == stack[-1]: 
                            destroyed = True
                        stack.pop()
                # if the current not destroyed, push to the stack
                if not destroyed:
                    stack.append(asteroids[i])
        return stack
