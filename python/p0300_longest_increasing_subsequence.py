from typing import List

def length_of_lis(nums: List[int]) -> int:
    # TODO fix - this doesn't work yet
    memo, prev = {}, -100000
    def dfs(prev: int, i: int) -> int:
        if i not in memo:
            if nums[i] > prev:
                is_increasing_val = 1
                prev = nums[i]
            else:
                is_increasing_val = 0 
            memo[i] = is_increasing_val
            for j in range(i + 1, len(nums)):
                memo[i] = max(memo[i], is_increasing_val + dfs(prev, j))
        return memo[i]
    return dfs(prev, 0)
