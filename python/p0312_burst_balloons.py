from typing import List

def max_coins_memo(nums: List[int]) -> int:
    memo = {}
    def dfs(l: int, r: int) -> int:
        if l > r:
            return 0
        if (l, r) not in memo:
            result = 0
            for i in range(l, r + 1):
                coins = (nums[l - 1] if l - 1 > -1 else 1) * nums[i] * (nums[r + 1] if r + 1 < len(nums) else 1)
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                result = max(result, coins)
            memo[(l, r)] = result
        return memo[(l, r)]
    return dfs(0, len(nums) - 1)

def max_coins_memo_extend_input(nums: List[int]) -> int:
    nums = [1] + [n for n in nums if n != 0] + [1]
    memo = {}
    def dfs(l: int, r: int) -> int:
        if l > r:
            return 0
        if (l, r) not in memo:
            result = 0
            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                result = max(result, coins)
            memo[(l, r)] = result
        return memo[(l, r)]
    return dfs(1, len(nums) - 2)

def max_coins_table_optimal(nums: List[int]) -> int:
    nums = [1] + [n for n in nums if n != 0] + [1]
    dp = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
    for r in range(2, len(nums)):
        for l in reversed(range(r - 1)):
            ends = nums[l] * nums[r]
            dp[l][r] = max(dp[l][i] + ends * nums[i] + dp[i][r] for i in range(l + 1, r))
    return dp[0][-1]
