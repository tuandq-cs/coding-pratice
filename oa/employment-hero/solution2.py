

from collections import deque
from math import inf


def solution(connections, name1, name2):
    adj = {}
    for r in connections:
        u, v = r.split(":")
        adj[u] = adj.get(u, [])
        adj[u].append(v)
        adj[v] = adj.get(v, [])
        adj[v].append(u)


    u, v = name1, name2
    if adj.get(u) is None or adj.get(v) is None:
        return -1
    visited = {}
    q = deque([])
    dist = {u: 0}
    q.append((u, 0))
    while len(q) != 0:
        node, l = q.pop()
        if visited.get(node):
            continue
        visited[node] = True
        for nei in adj[node]:
            dist[nei] = min(dist.get(nei, inf), l+1)
            q.append((nei, l+1))
    return dist.get(v, -1)

connections = ["fred:fred", "fred:joe", "joe:mary", "mary:fred", "mary:bill"]
name1 = "fred"
name2 = "fred"
    
out = solution(connections, name1, name2)
print(out)