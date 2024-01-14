from typing import List

def max_area_of_island(grid: List[List[int]]) -> int:
    max_area = 0
    visited = set()
    def bfs(x, y):
        queue = [(x, y)]
        curr_area = 0
        while queue:
            x, y = queue.pop(0)
            if (-1 < x < len(grid) and
                -1 < y < len(grid[0]) and
                grid[x][y] == 1 and
                (x, y) not in visited
            ):
                curr_area += 1
                visited.add((x, y))
                queue.append((x - 1, y))
                queue.append((x + 1, y))
                queue.append((x, y - 1))
                queue.append((x, y + 1))
        nonlocal max_area
        max_area = max(max_area, curr_area)
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 1 and (x, y) not in visited:
                bfs(x, y)
    return max_area

def max_area_of_island_mut(grid: List[List[int]]) -> int:
    max_area = 0
    def bfs(x, y) -> int:
        queue = [(x, y)]
        curr_area = 0
        while queue:
            x, y = queue.pop(0)
            if (-1 < x < len(grid) and
                -1 < y < len(grid[0]) and
                grid[x][y]
            ):
                curr_area += 1
                grid[x][y] = 0
                queue.append((x - 1, y))
                queue.append((x + 1, y))
                queue.append((x, y - 1))
                queue.append((x, y + 1))
        return curr_area
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y]:
                max_area = max(max_area, bfs(x, y))
    return max_area

