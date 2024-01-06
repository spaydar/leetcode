from typing import List

def subsets_with_dup(nums: List[int]) -> List[List[int]]:
    nums.sort()
    result = []
    curr = []
    def dfs(i: int):
        if i == len(nums):
            result.append(curr[:])
            return
        curr.append(nums[i])
        dfs(i + 1)
        curr.pop()
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        dfs(i + 1)
    dfs(0)
    return result
