from typing import List

def combination_sum_ii(candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    result = []
    curr = []
    def dfs(i: int, total: int):
        if total == target:
            result.append(curr[:])
            return
        if i == len(candidates) or total > target:
            return
        curr.append(candidates[i])
        dfs(i + 1, total + candidates[i])
        curr.pop()
        while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
            i += 1
        dfs(i + 1, total)
    dfs(0, 0)
    return result
