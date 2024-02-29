from collections import defaultdict
from heapq import heappop, heappush
from typing import List, Set, Tuple

def min_cost_connect_points_prims_compute_before(points: List[List[int]]) -> int:
    adj = defaultdict(list)
    for i in range(len(points)):
        x1, y1 = points[i]
        for j in range(i + 1, len(points)):
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
    def get_distance(a: int, b: int) -> int:
        x1, y1 = points[a]
        x2, y2 = points[b]
        return abs(x1 - x2) + abs(y1 - y2)
    total_cost = 0
    visited: Set[int] = set()
    min_heap: List[Tuple] = [(0, 0)]
    while len(visited) < len(points):
        cost, i = heappop(min_heap)
        if i in visited:
            continue
        total_cost += cost
        visited.add(i)
        for j in range(len(points)):
            if j != i and j not in visited:
                heappush(min_heap, (get_distance(i, j), j))
    return total_cost

def min_cost_connect_points_kruskals(points: List[List[int]]) -> int:
    parent = [i for i in range(len(points))]
    size = [1 for _ in range(len(points))]
    def find_parent(node: int) -> int:
        while node != parent[node]:
            parent[node] = parent[parent[node]]
            node = parent[node]
        return node
    def union(x: int, y: int) -> bool:
        x_par, y_par = find_parent(x), find_parent(y)
        if x_par == y_par:
            return False
        if size[x_par] > size[y_par]:
            parent[y_par] = x_par
            size[x_par] += 1
        else:
            parent[x_par] = y_par
            size[y_par] += 1
        return True
    min_heap = []
    for i in range(len(points)):
        x1, y1 = points[i]
        for j in range(i + 1, len(points)):
            x2, y2 = points[j]
            dist = abs(x1 - x2) + abs(y1 - y2)
            heappush(min_heap, (dist, i, j))
    total_cost = 0
    num_edges_added = 0
    while min_heap and num_edges_added < len(points) - 1:
        cost, i, j = heappop(min_heap)
        if union(i, j):
            total_cost += cost
            num_edges_added += 1
    return total_cost
