from typing import List

def find_redundant_connection(edges: List[List[int]]) -> List[int]:
    parent = [i for i in range(len(edges) + 1)]
    size = [1 for _ in range(len(edges) + 1)]
    def find_rep(node: int) -> int:
        while node != parent[node]:
            parent[node] = parent[parent[node]]
            node = parent[node]
        return node
    def union(x: int, y: int) -> bool:
        x_rep, y_rep = find_rep(x), find_rep(y)
        if x_rep == y_rep:
            return False
        if size[x_rep] > size[y_rep]:
            parent[y_rep] = x_rep
            size[x_rep] += 1
        else:
            parent[x_rep] = y_rep
            size[y_rep] += 1
        return True
    for x, y in edges:
        if not union(x, y):
            return [x, y]

def find_redundant_connection_recursive_find(edges: List[List[int]]) -> List[int]:
    parent = [i for i in range(len(edges) + 1)]
    size = [1 for _ in range(len(edges) + 1)]
    def find_rep(node: int) -> int:
        if parent[node] == node:
            return node
        parent[node] = parent[parent[node]]
        return find_rep(parent[node])
    def union(x: int, y: int) -> bool:
        x_rep, y_rep = find_rep(x), find_rep(y)
        if x_rep == y_rep:
            return False
        if size[x_rep] > size[y_rep]:
            parent[y_rep] = x_rep
            size[x_rep] += 1
        else:
            parent[x_rep] = y_rep
            size[y_rep] += 1
        return True
    for x, y in edges:
        if not union(x, y):
            return [x, y]
