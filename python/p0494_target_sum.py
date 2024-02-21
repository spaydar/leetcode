from typing import List

def find_target_sum_ways_memo(nums: List[int], target: int) -> int:
    memo = {}
    def dfs(remaining: int, i: int) -> int:
        if i == len(nums):
            return 1 if remaining == 0 else 0
        if (remaining, i) not in memo:
            memo[(remaining, i)] = dfs(remaining + nums[i], i + 1) + dfs(remaining - nums[i], i + 1)
        return memo[(remaining, i)]
    return dfs(target, 0)

def find_target_sum_ways_table_2d(nums: List[int], target: int) -> int:
    # TODO
    # dp = []
    return -1
