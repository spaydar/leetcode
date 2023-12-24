from typing import List

def number_of_islands(grid: List[List[str]]) -> int:
    visited = set()
    def bfs(x: int, y: int) -> None:
        queue = [(x, y)]
        while queue:
            x, y = queue.pop(0)
            if -1 < x < len(grid) and -1 < y < len(grid[x]) and grid[x][y] == '1' and (x, y) not in visited:
                visited.add((x, y))
                queue.append((x - 1, y))
                queue.append((x + 1, y))
                queue.append((x, y - 1))
                queue.append((x, y + 1))
    count = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == '1' and (x, y) not in visited:
                bfs(x, y)
                count += 1
    return count
