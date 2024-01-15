from typing import List, Set, Tuple

def pacific_atlantic(heights: List[List[int]]) -> List[List[int]]:
    NUM_ROWS, NUM_COLS = len(heights), len(heights[0])
    flows_to_pacific = set()
    flows_to_atlantic = set()
    def bfs(x: int, y: int, prev_height: int, visited: Set[Tuple[int, int]]):
        queue = [(x, y, prev_height)]
        while queue:
            x, y, prev_height = queue.pop(0)
            if (-1 < x < NUM_ROWS and
                -1 < y < NUM_COLS and
                heights[x][y] >= prev_height and
                (x, y) not in visited
            ):
                visited.add((x, y))
                queue.append((x - 1, y, heights[x][y]))
                queue.append((x + 1, y, heights[x][y]))
                queue.append((x, y - 1, heights[x][y]))
                queue.append((x, y + 1, heights[x][y]))
    for x in range(NUM_ROWS):
        bfs(x, 0, -1, flows_to_pacific)
        bfs(x, NUM_COLS - 1, -1, flows_to_atlantic)
    for y in range(NUM_COLS):
        bfs(0, y, -1, flows_to_pacific)
        bfs(NUM_ROWS - 1, y, -1, flows_to_atlantic)
    return [list(t) for t in flows_to_pacific.intersection(flows_to_atlantic)]
