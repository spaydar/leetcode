from collections import defaultdict
from typing import List

def is_valid_sudoku_1_set(board: List[List[str]]) -> bool:
    nums_seen = set()
    def cell_is_valid(x: int, y: int) -> bool:
        val = board[x][y]
        if val != '.':
            if val in nums_seen:
                return False
            nums_seen.add(val)
        return True
    for x in range(9):
        nums_seen.clear()
        for y in range(9):
            if not cell_is_valid(x, y):
                return False
    for y in range(9):
        nums_seen.clear()
        for x in range(9):
            if not cell_is_valid(x, y):
                return False
    for x_step in range(0, 9, 3):
        for y_step in range(0, 9, 3):
            nums_seen.clear()
            for x in range(3):
                for y in range(3):
                    if not cell_is_valid(x + x_step, y + y_step):
                        return False
    return True

def is_valid_sudoku_multiple_sets(board: List[List[str]]) -> bool:
    row_sets = defaultdict(set)
    col_sets = defaultdict(set)
    sqr_sets = defaultdict(set)
    for x in range(9):
        for y in range(9):
            val = board[x][y]
            if val == '.':
                continue
            sqr_key = (x // 3, y // 3)
            if val in row_sets[x] or val in col_sets[y] or val in sqr_sets[sqr_key]:
                return False
            row_sets[x].add(val)
            col_sets[y].add(val)
            sqr_sets[sqr_key].add(val)
    return True
