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

def longest_increasing_path_2d(matrix: List[List[int]]) -> int:
    return -1
