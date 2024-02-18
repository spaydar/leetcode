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

def unique_paths_table(m: int, n: int) -> int:
    table = [1 for _ in range(n)]
    for _ in range(m - 1):
        for i in range(1, n):
            table[i] += table[i - 1]
    return table[-1]
