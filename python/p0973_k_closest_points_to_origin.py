import heapq
from typing import List

def k_closest(points: List[List[int]], k: int) -> List[List[int]]:
    for p in points:
        p.insert(0, p[0] ** 2 + p[1] ** 2)
    heapq.heapify(points)
    result = []
    while len(result) < k:
        result.append(heapq.heappop(points)[1:])
    return result
