from typing import List, Set, Tuple

def rotting_oranges(grid: List[List[int]]) -> int:
    from collections import deque
    NUM_ROWS, NUM_COLS = len(grid), len(grid[0])
    visited: Set[Tuple[int, int]] = set()
    time, num_fresh = 0, 0
    queue = deque()
    for x in range(NUM_ROWS):
        for y in range(NUM_COLS):
            if grid[x][y] == 1:
                num_fresh += 1
            elif grid[x][y] == 2:
                queue.append((x, y, 0))
    while queue:
        x, y, t = queue.popleft()
        if (-1 < x < NUM_ROWS and
            -1 < y < NUM_COLS and
            grid[x][y] and
            (x, y) not in visited
        ):
            visited.add((x, y))
            time = max(time, t)
            if grid[x][y] == 1:
                num_fresh -= 1
            queue.append((x + 1, y, t + 1))
            queue.append((x - 1, y, t + 1))
            queue.append((x, y + 1, t + 1))
            queue.append((x, y - 1, t + 1))
    return time if num_fresh == 0 else -1

def rotting_oranges_mut(grid: List[List[int]]) -> int:
    from collections import deque
    NUM_ROWS, NUM_COLS = len(grid), len(grid[0])
    time, num_fresh = 0, 0
    queue = deque()
    for x in range(NUM_ROWS):
        for y in range(NUM_COLS):
            if grid[x][y] == 1:
                num_fresh += 1
            elif grid[x][y] == 2:
                queue.append((x, y, 0))
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while queue:
        x, y, t = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (-1 < nx < NUM_ROWS and
                -1 < ny < NUM_COLS and
                grid[nx][ny] == 1
            ):
                grid[nx][ny] = 2
                num_fresh -= 1
                time = max(time, t + 1)
                queue.append((nx, ny, t + 1))
    return time if num_fresh == 0 else -1
