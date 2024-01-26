from typing import List

def min_cost_climbing_stairs_memo(cost: List[int]) -> int:
    memo = {}
    def dfs(i: int) -> int:
        if i >= len(cost):
            return 0
        if i == len(cost) - 1:
            return cost[i]
        if i not in memo:
            memo[i] = min(cost[i] + dfs(i + 1), cost[i] + dfs(i + 2))
        return memo[i]
    return min(dfs(0), dfs(1))

def min_cost_climbing_stairs_table(cost: List[int]) -> int:
    table = cost[:]
    for i in range(len(cost) - 3, -1, -1):
        table[i] += min(table[i + 1], table[i + 2])
    return min(table[0], table[1])

def min_cost_climbing_stairs_constant(cost: List[int]) -> int:
    i, left, right = len(cost) - 3, cost[-2], cost[-1]
    while i > -1:
        next = cost[i] + min(left, right)
        right = left
        left = next
        i -= 1
    return min(left, right)
