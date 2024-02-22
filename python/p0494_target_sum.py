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
    total = sum(nums)
    if target > total:
        return 0
    dp = [[0 for _ in range(2 * total + 1)] for _ in nums]
    dp[0][total - nums[0]] = 1
    dp[0][total + nums[0]] += 1
    for i in range(1, len(nums)):
        for j in range(nums[i], 2 * total + 1 - nums[i]):
            dp[i][j - nums[i]] += dp[i - 1][j]
            dp[i][j + nums[i]] += dp[i - 1][j]
    return dp[-1][total + target]

def find_target_sum_ways_table_1d(nums: List[int], target: int) -> int:
    total = sum(nums)
    if target > total:
        return 0
    prev = [0 for _ in range(2 * total + 1)]
    curr = [0 for _ in range(2 * total + 1)]
    prev[total - nums[0]] = 1
    prev[total + nums[0]] += 1
    for i in range(1, len(nums)):
        for j in range(nums[i], 2 * total + 1 - nums[i]):
            curr[j - nums[i]] += prev[j]
            curr[j + nums[i]] += prev[j]
        for i in range(len(prev)):
            prev[i] = curr[i]
            curr[i] = 0
    return prev[total + target]

def find_target_sum_ways_table_1d_optimal(nums: List[int], target: int) -> int:
    if abs(sum(nums)) < abs(target) or (target + sum(nums)) % 2 != 0:
        return 0
    target = (target + sum(nums)) // 2
    dp = [0 for _ in range(target + 1)]
    dp[0] = 1
    for num in nums:
        for j in range(target, num - 1, -1):
            dp[j] += dp[j - num]
    return dp[target]
