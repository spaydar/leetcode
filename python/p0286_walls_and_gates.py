from typing import List

# Implementing solution for problem as described on neetcode.io: https://neetcode.io/problems/islands-and-treasure
def walls_and_gates(grid: List[List[int]]):
    from collections import deque
    queue = deque()
    NUM_ROWS, NUM_COLS, INF = len(grid), len(grid[0]), 2147483647
    for x in range(NUM_ROWS):
        for y in range(NUM_COLS):
            if grid[x][y] == 0:
                grid[x][y] = INF
                queue.append((x, y, 0))
    while queue:
        x, y, d = queue.popleft()
        if (-1 < x < NUM_ROWS and
            -1 < y < NUM_COLS and
            grid[x][y] == INF
        ):
            grid[x][y] = d
            queue.append((x - 1, y, d + 1))
            queue.append((x + 1, y, d + 1))
            queue.append((x, y - 1, d + 1))
            queue.append((x, y + 1, d + 1))
