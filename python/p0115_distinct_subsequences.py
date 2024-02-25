def num_distinct_memo(s: str, t: str) -> int:
    memo = {}
    def dfs(i: int, j: int) -> int:
        if j == len(t):
            return 1
        if i == len(s) or len(s) - i < len(t) - j:
            return 0
        if (i, j) not in memo:
            if s[i] == t[j]:
                memo[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                memo[(i, j)] = dfs(i + 1, j)
        return memo[(i, j)]
    return dfs(0, 0)

def num_distinct_table_2d(s: str, t: str) -> int:
    dp = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]
    for i in range(len(s) + 1):
        dp[i][-1] = 1
    for i in range(len(s) - 1, -1, -1):
        for j in range(len(t) - 1, -1, -1):
            if len(s) - i < len(t) - j:
                break
            dp[i][j] = dp[i + 1][j]
            if s[i] == t[j]:
                dp[i][j] += dp[i + 1][j + 1]
    return dp[0][0]

def num_distinct_table_1d(s: str, t: str) -> int:
    prev = [0 for _ in range(len(t) + 1)]
    prev[-1] = 1
    curr = prev[:]
    for i in range(len(s) - 1, -1, -1):
        for j in range(len(t) - 1, -1, -1):
            if len(s) - i < len(t) - j:
                break
            curr[j] = prev[j]
            if s[i] == t[j]:
                curr[j] += prev[j + 1]
        for k in range(len(curr) - 1):
            prev[k] = curr[k]
            curr[k] = 0
    return prev[0]
