from collections import defaultdict
from heapq import heappop, heappush
from typing import List, Tuple, Set

def network_delay_time(times: List[List[int]], n: int, k: int) -> int:
    adj = defaultdict(list)
    for src, dest, cost in times:
        adj[src].append((cost, dest))
    visited: Set[int] =  set()
    min_heap: List[Tuple[int, int]] = [(0, k)]
    while min_heap:
        total_cost, node = heappop(min_heap)
        if node in visited:
            continue
        visited.add(node)
        if len(visited) == n:
            return total_cost
        for next_cost, dest in adj[node]:
            heappush(min_heap, (total_cost + next_cost, dest))
    return -1
