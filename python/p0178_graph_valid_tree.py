from typing import List

def is_valid_tree(n: int, edges: List[List[int]]) -> bool:
    if len(edges) != n - 1:
        return False
    parent = [i for i in range(n)]
    size = [1 for _ in range(n)]
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
    for x, y in edges:
        if not union(x, y):
            return False
    return True
