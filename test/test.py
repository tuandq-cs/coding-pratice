

from typing import List


def compute(visited: List[bool], weights: List[float]):
    residual = 0
    remain_sum_weight = 0
    for i in range(len(weights)):
        if weights[i] >= 0.1:
            residual += weights[i] - 0.1
            weights[i] = 0.1
        else:
            remain_sum_weight += weights[i]
    for i in range(len(weights)):
        if weights[i] < 0.1:
            weights[i] = weights[i] * \
                (residual+remain_sum_weight) / remain_sum_weight
    return residual


def adjustWeights(weights: List[float]) -> List[float]:
    if len(weights) < 10:
        return []
    while True:
        if compute(weights) == 0:
            break
    return weights


def computeWithGroup(groups: List[int], weights: List[float]):
    mGroup = {}
    for i in range(len(weights)):
        g = groups[i]
        if mGroup.get(g) is None:
            mGroup[g] = 0
        mGroup[g] += weights[i]
    residual = 0
    remain_sum_weight = 0
    for g in mGroup:
        if mGroup[g] >= 0.3:
            residual += mGroup[g] - 0.3
            mGroup[g] = 0.3
        else:
            remain_sum_weight += mGroup[g]
    for i in range(len(weights)):
        if mGroup[groups[i]] == 0.3 or weights[i] == 0.1:
            remain_sum_weight -= 0.1

    for i in range(len(weights)):
        if mGroup[groups[i]] < 0.3 and weights[i] < 0.1:
            weights[i] = weights[i] * \
                (residual+remain_sum_weight) / remain_sum_weight
    return residual


def getGroupWeight(groups, weights):
    mGroup = {}
    for i in range(len(weights)):
        g = groups[i]
        if mGroup.get(g) is None:
            mGroup[g] = 0
        mGroup[g] += weights[i]
    return mGroup


def adjustWithGroup(groups: List[int], weights: List[float]) -> List[float]:
    if len(weights) < 10:
        return []
    visited = [False for _ in range(len(weights))]

    def solve():
        mGroup = getGroupWeight(groups, weights)
        residual = 0
        remain_sum_weight = 0
        for g in mGroup:
            if mGroup[g] == 0.3:
                continue
            if mGroup[g] > 0.3:
                residual += mGroup[g] - 0.3
            else:
                remain_sum_weight += mGroup[g]
        for i in range(len(weights)):
            if mGroup[groups[i]] < 0.3 and weights[i] == 0.1:
                remain_sum_weight -= 0.1

        for i in range(len(weights)):
            if mGroup[groups[i]] >= 0.3:
                weights[i] *= 0.3 / mGroup[groups[i]]
                visited[i] = True
            if mGroup[groups[i]] < 0.3 and weights[i] < 0.1:
                weights[i] = weights[i] * \
                    (residual+remain_sum_weight) / remain_sum_weight
        return residual


weights = [0.2, 0.15, 0.13, 0.12, 0.1, 0.1, 0.1, 0.06, 0.02, 0.015, 0.005]
out = adjustWeights(weights)
print(weights)
print(sum(weights))
