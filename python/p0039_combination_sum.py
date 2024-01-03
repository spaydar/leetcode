from typing import List

def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    result = []
    curr = []
    def dfs(i: int, curr_sum):
        if curr_sum == target:
            result.append(curr[:])
        elif curr_sum < target and i < len(candidates):
            curr.append(candidates[i])
            dfs(i, curr_sum + candidates[i])
            curr.pop()
            dfs(i + 1, curr_sum)
    dfs(0, 0)
    return result
