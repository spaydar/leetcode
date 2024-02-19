def unique_paths_memo(m: int, n: int) -> int:
    memo = {}
    def dfs(x: int, y: int) -> int:
        if x == m or y == n:
            return 0
        if x == m - 1 and y == n - 1:
            return 1
        if (x, y) not in memo:
            memo[(x, y)] = dfs(x + 1, y) + dfs(x, y + 1)
        return memo[(x, y)]
    return dfs(0, 0)

def unique_paths_table_2d(m: int, n: int) -> int:
    dp = [[0 for _ in range(n + 1)] for _ in range(m)]
    for i in range(1, n + 1):
        dp[0][i] = 1
    for i in range(1, m):
        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[-1][-1]

def unique_paths_table_1d(m: int, n: int) -> int:
    if n > m:
        m, n = n, m
    table = [1 for _ in range(n)]
    for _ in range(m - 1):
        for i in range(1, n):
            table[i] += table[i - 1]
    return table[-1]
