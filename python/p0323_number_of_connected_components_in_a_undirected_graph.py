from typing import List

def count_components(n: int, edges: List[List[int]]) -> int:
    num_components = n
    parent = [i for i in range(n)]
    size = [1 for _ in range(n)]
    def find_parent(node: int) -> int:
        while node != parent[node]:
            parent[node] = parent[parent[node]]
            node = parent[node]
        return node
    def union(x: int, y: int):
        x_par, y_par = find_parent(x), find_parent(y)
        if x_par == y_par:
            return
        if size[x_par] > size[y_par]:
            parent[y_par] = x_par
            size[x_par] += 1
        else:
            parent[x_par] = y_par
            size[y_par] += 1
        nonlocal num_components
        num_components -= 1
    for x, y in edges:
        union(x, y)
    return num_components
