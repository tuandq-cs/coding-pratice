from typing import List


def getGroupWeight(groups, weights):
    gWeight = {}
    for i in range(len(weights)):
        g = groups[i]
        if gWeight.get(g) is None:
            gWeight[g] = 0
        gWeight[g] += weights[i]
    return gWeight


def balanceWeights(groups: List[int], weights: List[float], visited: set):
    residual = 0.0
    remainSum = 0.0
    for i in range(len(weights)):
        if groups[i] in visited or abs(weights[i] - 0.1) < 1e-10:
            continue
        if weights[i] > 0.1:
            residual += weights[i] - 0.1
            weights[i] = 0.1
        else:
            remainSum += weights[i]
    for i in range(len(weights)):
        if groups[i] in visited:
            continue
        if weights[i] < 0.1:
            weights[i] = weights[i] * (1 + residual/remainSum)
    return residual


def adjustWeights(groups: List[int], weights: List[float], visited: set):
    while True:
        if balanceWeights(groups, weights, visited) == 0:
            break
    return weights


def balanceGroups(groups: List[int], weights: List[float], visited: set):
    adjustWeights(groups, weights, visited)
    gWeight = getGroupWeight(groups, weights)
    residual = 0
    remainSum = 0
    for g in gWeight:
        if g in visited or abs(gWeight[g] - 0.3) < 1e-6:
            continue
        if gWeight[g] > 0.3:
            residual += gWeight[g] - 0.3
            visited.add(g)
        else:
            remainSum += gWeight[g]
    for i in range(len(weights)):
        if groups[i] in visited:
            continue
        if (weights[i] - 0.1) < 1e-6:
            remainSum -= 0.1

    for i in range(len(weights)):
        if groups[i] in visited:
            weights[i] *= 0.3 / gWeight[groups[i]]
            continue
        if gWeight[groups[i]] < 0.3 and weights[i] < 0.1:
            weights[i] = weights[i] * \
                (residual+remainSum) / remainSum
    return residual


def adjustGroups(groups: List[int], weights: List[float]) -> List[float]:
    if len(weights) < 10:
        return []
    gWeight = getGroupWeight(groups, weights)
    visited = set()
    while len(visited) < len(gWeight):
        if balanceGroups(groups, weights, visited) == 0:
            break
    return weights


weights = [0.00245,
           0.006287,
           0.005399,
           0.008407,
           0.003334,
           0.005315,
           0.006322,
           0.007387,
           0.036308,
           0.00885,
           0.020869,
           0.011074,
           0.170716,
           0.011365,
           0.021128,
           0.030647,
           0.004884,
           0.006601,
           0.007072,
           0.14334,
           0.017846,
           0.002219,
           0.013101,
           0.016925,
           0.016885,
           0.083306,
           0.098327,
           0.004709,
           0.008544,
           0.003831,
           0.03744,
           0.017608,
           0.008716,
           0.008319,
           0.003253,
           0.007926,
           0.010998,
           0.004254,
           0.012328,
           0.10571]
groups = [
    1,
    3,
    2,
    2,
    1,
    4,
    4,
    5,
    4,
    3,
    4,
    3,
    1,
    5,
    2,
    1,
    2,
    5,
    4,
    5,
    3,
    4,
    2,
    2,
    2,
    1,
    5,
    2,
    3,
    3,
    4,
    1,
    1,
    2,
    3,
    4,
    1,
    1,
    3,
    5
]
# adjustGroups(groups, weights)
adjustWeights(groups, weights, set())
print(weights)
