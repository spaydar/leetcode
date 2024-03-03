from typing import List

def search_matrix(matrix: List[List[int]], target: int) -> bool:
    ROWS, COLS = len(matrix), len(matrix[0])
    bot, top = 0, ROWS - 1
    while bot <= top:
        row = bot + (top - bot) // 2
        if matrix[row][0] <= target <= matrix[row][COLS - 1]:
            break
        if matrix[row][0] >= target:
            top = row - 1
        else:
            bot = row + 1
    if bot > top:
        return False
    row = bot + (top - bot) // 2
    l, r = 0, COLS - 1
    while l <= r:
        m = l + (r - l) // 2
        if matrix[row][m] == target:
            return True
        if matrix[row][m] > target:
            r = m - 1
        else:
            l = m + 1
    return False

def search_matrix_flattened(matrix: List[List[int]], target: int) -> bool:
    ROWS, COLS = len(matrix), len(matrix[0])
    l, r = 0, ROWS * COLS - 1
    while l <= r:
        m = l + (r - l) // 2
        x, y = m // COLS, m % COLS
        if matrix[x][y] == target:
            return True
        if matrix[x][y] < target:
            l = m + 1
        else:
            r = m - 1
    return False
