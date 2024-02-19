def longest_common_subsequence_memo(text1: str, text2: str) -> int:
    memo = {}
    def dfs(x: int, y: int) -> int:
        if x == len(text1) or y == len(text2):
            return 0
        if (x, y) not in memo:
            if text1[x] == text2[y]:
                memo[(x, y)] = 1 + dfs(x + 1, y + 1)
            else:
                memo[(x, y)] = max(dfs(x + 1, y), dfs(x, y + 1))
        return memo[(x, y)]
    return dfs(0, 0)

def longest_common_subsequence_table_2d(text1: str, text2: str) -> int:
    dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
    for i in range(1, len(text1) + 1):
        for j in range(1, len(text2) + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]

def longest_common_subsequence_table_1d(text1: str, text2: str) -> int:
    short, long = (text1, text2) if len(text1) <= len(text2) else (text2, text1)
    prev_row = [0 for _ in range(len(short) + 1)]
    for c in long:
        curr_row = [0 for _ in range(len(short) + 1)]
        for i in range(1, len(short) + 1):
            if short[i - 1] == c:
                curr_row[i] = 1 + prev_row[i - 1]
            else:
                curr_row[i] = max(curr_row[i - 1], prev_row[i])
        prev_row = curr_row
    return prev_row[-1]
