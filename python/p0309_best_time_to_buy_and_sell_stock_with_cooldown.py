from typing import List

def max_profit_memo(prices: List[int]) -> int:
    memo = {}
    def dfs(t: int, has_stock: bool) -> int:
        if t >= len(prices):
            return 0
        if not (t, has_stock) in memo:
            if has_stock:
                memo[(t, has_stock)] = max(dfs(t + 2, False) + prices[t], dfs(t + 1, has_stock))
            else:
                memo[(t, has_stock)] = max(dfs(t + 1, True) - prices[t], dfs(t + 1, has_stock))
        return memo[(t, has_stock)]
    return dfs(0, False)

def max_profit_table_2d(prices: List[int]) -> int:
    dp = [[0 for _ in range(2)] for _ in range(len(prices) + 2)]
    for t in range(len(prices) - 1, -1, -1):
        dp[t][0] = max(dp[t + 1][1] - prices[t], dp[t + 1][0])
        dp[t][1] = max(dp[t + 2][0] + prices[t], dp[t + 1][1])
    return dp[0][0]

def max_profit_table_1d(prices: List[int]) -> int:
    curr, one, two = [0, 0], [0, 0], [0, 0]
    for t in range(len(prices) - 1, -1, -1):
        curr[0] = max(one[1] - prices[t], one[0])
        curr[1] = max(two[0] + prices[t], one[1])
        two, one = one, curr
        curr = [0, 0]
    return one[0]

def max_profit_table_1d_mut(prices: List[int]) -> int:
    curr, one, two = [0, 0], [0, 0], [0, 0]
    for t in range(len(prices) - 1, -1, -1):
        curr[0] = max(one[1] - prices[t], one[0])
        curr[1] = max(two[0] + prices[t], one[1])
        two[0], two[1] = one[0], one[1]
        one[0], one[1] = curr[0], curr[1]
        curr[0], curr[1] = 0, 0
    return one[0]

def max_profit_table_1d_forward(prices: List[int]) -> int:
    # TODO try with forward iteration by inverting buy & sell, taking min, and multiplying final result by -1
    return -1
