def is_match_memo(s: str, p: str) -> bool:
    memo = {}
    def dfs(i: int, j: int) -> bool:
        if i == len(s) and j >= len(p):
            return True
        if j >= len(p):
            return False
        if (i, j) not in memo:
            chars_match = i < len(s) and (p[j] == '.' or s[i] == p[j])
            if j < len(p) - 1 and p[j + 1] == '*':
                memo[(i, j)] = dfs(i, j + 2) or (chars_match and dfs(i + 1, j))
            elif chars_match:
                memo[(i, j)] = dfs(i + 1, j + 1)
            else:
                memo[(i, j)] = False
        return memo[(i, j)]
    return dfs(0, 0)

def is_match_table_2d(s: str, p: str) -> bool:
    # TODO this isn't working for s = "aabcbcbcaccbcaabc" and p = ".*a*aa*.*b*.c*.*a*"
    dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
    dp[-1][-1] = True
    for j in range(len(p) - 1):
        if p[j + 1] == '*':
            dp[-1][j] = dp[-1][j + 2]
    for i in reversed(range(len(s))):
        for j in reversed(range(len(p))):
            chars_match = p[j] == '.' or s[i] == p[j]
            if j < len(p) - 1 and p[j + 1] == '*':
                dp[i][j] = dp[i][j + 2] or (chars_match and dp[i + 1][j])
            else:
                dp[i][j] = chars_match and dp[i + 1][j + 1]
    return dp[0][0]
