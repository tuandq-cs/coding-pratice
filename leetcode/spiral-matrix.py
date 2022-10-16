# https://leetcode.com/problems/spiral-matrix/


# Simple explanation
# https://leetcode.com/problems/spiral-matrix/discuss/20599/Super-Simple-and-Easy-to-Understand-Solution

from queue import Queue
from typing import List

def spiralOrder(matrix: List[List[int]]) -> List[int]:
    m, n = len(matrix[0]), len(matrix)
    di = Queue(0)
    di.put('r')
    di.put('d')
    di.put('l')
    di.put('u')
    
    cur = (0, 0)
    my_map = {'0.0': 1}
    result = [matrix[0][0]]

    while not di.empty():
        d = di.get()
        x, y = cur
        cond_r = d == "r" and (x + 1 == m or my_map.get(f'{x+1}.{y}'))
        cond_d = d == "d" and (y + 1 == n or my_map.get(f'{x}.{y+1}'))
        cond_l = d == "l" and (x - 1 < 0 or my_map.get(f'{x-1}.{y}'))
        cond_u = d == "u" and (y - 1 < 0 or my_map.get(f'{x}.{y-1}'))
        if cond_r or cond_d or cond_l or cond_u:
            continue
        cords = [(n_x, y) for n_x in range(x+1, m)] if d == "r" else \
                [(x, n_y) for n_y in range(y+1, n)] if d == "d" else \
                [(n_x, y) for n_x in range(x-1, -1, -1)] if d == "l" else \
                [(x, n_y) for n_y in range(y-1, -1, -1)]
        for nx, ny in cords:
            k = f'{nx}.{ny}'
            if my_map.get(k):
                break
            my_map[k] = 1
            cur = (nx, ny)
            result.append(matrix[ny][nx])
        di.put(d)
    return result
        

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
result = spiralOrder(matrix)
print(result)


        