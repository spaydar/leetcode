from typing import List, Set, Tuple

def flip_surrounded(board: List[List[str]]) -> None:
    NUM_ROWS, NUM_COLS = len(board), len(board[0])
    not_surrounded: Set[Tuple[int, int]] = set()
    def dfs(x: int, y: int):
        stack = [(x, y)]
        while stack:
            x, y = stack.pop()
            if (-1 < x < NUM_ROWS and
                -1 < y < NUM_COLS and
                board[x][y] == 'O' and
                (x, y) not in not_surrounded
            ):
                not_surrounded.add((x, y))
                stack.append((x - 1, y))
                stack.append((x + 1, y))
                stack.append((x, y - 1))
                stack.append((x, y + 1))
    for x in range(NUM_ROWS):
        dfs(x, 0)
        dfs(x, NUM_COLS - 1)
    for y in range(NUM_COLS):
        dfs(0, y)
        dfs(NUM_ROWS - 1, y)
    for x in range(NUM_ROWS):
        for y in range(NUM_COLS):
            if (x, y) not in not_surrounded:
                board[x][y] = 'X'
