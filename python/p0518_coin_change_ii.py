from typing import List, reveal_type

def change_memo(amount: int, coins: List[int]) -> int:
    memo = {}
    def dfs(remaining: int, i: int) -> int:
        if remaining < 0 or i == len(coins):
            return 0
        if remaining == 0:
            return 1
        if (remaining, i) not in memo:
            memo[(remaining, i)] = dfs(remaining - coins[i], i) + dfs(remaining, i + 1)
        return memo[(remaining, i)]
    return dfs(amount, 0)

def change_table_2d(amount: int, coins: List[int]) -> int:
    dp = [[0 for _ in range(len(coins) + 1)] for _ in range(amount + 1)]
    for i in range(len(coins)):
        dp[0][i] = 1
    for a in range(1, amount + 1):
        for i in range(len(coins) - 1, -1, -1):
            dp[a][i] = dp[a][i + 1]
            if a - coins[i] > -1:
                dp[a][i] += dp[a - coins[i]][i]
    return dp[-1][0]

def change_table_1d(amount: int, coins: List[int]) -> int:
    prev, curr = [0 for _ in range(amount + 1)], [0 for _ in range(amount + 1)]
    prev[0], curr[0] = 1, 1
    for i in range(len(coins) - 1, -1, -1):
        for a in range(1, amount + 1):
            curr[a] = prev[a]
            if a - coins[i] > -1:
                curr[a] += curr[a - coins[i]]
        for a in range(1, amount + 1):
            prev[a] = curr[a]
            curr[a] = 0
    return prev[-1]

def change_table_1_array(amount: int, coins: List[int]) -> int:
    coins = [c for c in coins if c <= amount] # only consider eligible coins
    coins.sort(reverse=True)                  # sort coins so subproblems are solved in order
    dp = [0 for _ in range(amount + 1)]
    dp[0] = 1
    for coin in coins:
        dp[coin] = 1
        for i in range(coin, amount - coin + 1):
            dp[i + coin] += dp[i]
    return dp[-1]
