from typing import List

def longest_increasing_path_memo(matrix: List[List[int]]) -> int:
    memo, ROWS, COLS = {}, len(matrix), len(matrix[0])
    def dfs(x, y, prev) -> int:
        if (x < 0 or x == ROWS or
            y < 0 or y == COLS or
            matrix[x][y] <= prev
        ):
            return 0
        if (x, y) not in memo:
            result = 0
            for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                result = max(result, 1 + dfs(i , j, matrix[x][y]))
            memo[(x, y)] = result
        return memo[(x, y)]
    result = -1
    for x in range(ROWS):
        for y in range(COLS):
            result = max(result, dfs(x, y, -1))
    return result

def longest_increasing_path_table(matrix: List[List[int]]) -> int:
    ROWS, COLS = len(matrix), len(matrix[0])
    dp = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    def dfs(x: int, y: int, prev: int) -> int:
        if (x < 0 or x == ROWS or
            y < 0 or y == COLS or
            matrix[x][y] <= prev
        ):
            return 0
        if not dp[x][y]:
            dp[x][y] = 1 + max(
                dfs(x - 1, y, matrix[x][y]),
                dfs(x + 1, y, matrix[x][y]),
                dfs(x, y - 1, matrix[x][y]),
                dfs(x, y + 1, matrix[x][y])
            )
        return dp[x][y]
    result = -1
    for x in range(ROWS):
        for y in range(COLS):
            result = max(result, dfs(x, y, -1))
    return result

def longest_increasing_path_table_inline(matrix: List[List[int]]) -> int:
    ROWS, COLS = len(matrix), len(matrix[0])
    dp = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    def dfs(x: int, y: int) -> int:
        if not dp[x][y]:
            dp[x][y] = 1 + max(
                dfs(x - 1, y) if x and matrix[x - 1][y] < matrix[x][y] else 0,
                dfs(x + 1, y) if x < ROWS - 1 and matrix[x + 1][y] < matrix[x][y] else 0,
                dfs(x, y - 1) if y and matrix[x][y - 1] < matrix[x][y] else 0,
                dfs(x, y + 1) if y < COLS - 1 and matrix[x][y + 1] < matrix[x][y] else 0
            )
        return dp[x][y]
    result = -1
    for x in range(ROWS):
        for y in range(COLS):
            result = max(result, dfs(x, y))
    return result
