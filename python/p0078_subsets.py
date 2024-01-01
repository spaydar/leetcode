from typing import List

def subsets(nums: List[int]) -> List[List[int]]:
    result = []
    subset = []
    def dfs(i: int):
        if i == len(nums):
            result.append(subset[:])
            if len(subset) > 0:
                subset.pop()
            return
        subset.append(nums[i])
        dfs(i + 1)
        dfs(i + 1)
    dfs(0)
    return result
