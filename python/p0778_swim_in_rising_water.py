from heapq import heappop, heappush
from typing import List, Set, Tuple

def swim_in_water_djikstras(grid: List[List[int]]) -> int:
    visited: Set[Tuple[int, int]] = set()
    min_heap: List[Tuple[int, int, int]] = [(grid[0][0], 0, 0)]
    visited.add((0, 0))
    while min_heap:
        total_cost, x, y = heappop(min_heap)
        if x == y == len(grid) - 1:
            return total_cost
        for i, j in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if -1 < i < len(grid) and -1 < j < len(grid) and (i, j) not in visited:
                visited.add((i, j))
                heappush(min_heap, (max(total_cost, grid[i][j]), i, j))
    return -1

def swim_in_water_binary_search(grid: List[List[int]]) -> int:
    return -1
