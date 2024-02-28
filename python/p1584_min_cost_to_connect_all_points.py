from collections import defaultdict
from heapq import heappop, heappush
from typing import List, Set, Tuple

def min_cost_connect_points_prims_compute_before(points: List[List[int]]) -> int:
    adj = defaultdict(list)
    for i in range(len(points)):
        x1, y1 = points[i]
        for j in range(i, len(points)):
            x2, y2 = points[j]
            dist = abs(x1 - x2) + abs(y1 - y2)
            adj[i].append((dist, j))
            adj[j].append((dist, i))
    total_cost = 0
    visited: Set[int] = set()
    min_heap: List[Tuple] = [(0, 0)]
    while len(visited) < len(points):
        cost, i = heappop(min_heap)
        if i in visited:
            continue
        total_cost += cost
        visited.add(i)
        for adj_cost, j in adj[i]:
            if j not in visited:
                heappush(min_heap, (adj_cost, j))
    return total_cost

def min_cost_connect_points_prims_compute_during(points: List[List[int]]) -> int:
    # TODO
    return -1

def min_cost_connect_points_kruskals(points: List[List[int]]) -> int:
    # TODO
    return -1
