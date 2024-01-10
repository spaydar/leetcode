from typing import List, Set, Tuple

def word_exists(board: List[List[str]], word: str) -> bool:
    NUM_ROWS, NUM_COLS = len(board), len(board[0])
    visited: Set[Tuple[int, int]] = set()
    def dfs(i: int, j: int, c: int) -> bool:
        if c == len(word):
            return True
        if (i < 0 or j < 0 or
            i == NUM_ROWS or j == NUM_COLS or
            (i, j) in visited or
            board[i][j] != word[c]):
            return False
        visited.add((i, j))
        exists = (dfs(i - 1, j, c + 1) or
                  dfs(i + 1, j, c + 1) or
                  dfs(i, j - 1, c + 1) or
                  dfs(i, j + 1, c + 1))
        visited.remove((i, j))
        return exists
    for i in range(NUM_ROWS):
        for j in range(NUM_COLS):
            if dfs(i, j, 0):
                return True
    return False
