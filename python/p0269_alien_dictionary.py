from collections import defaultdict
from typing import List

def alien_order(words: List[str]) -> str:
    # TODO this isn't working yet
    adj = defaultdict(set)
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        min_len = min(len(w1), len(w2))
        if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
            return ''
        for j in range(min_len):
            if w1[j] != w2[j]:
                adj[w1[j]].add(w2[j])
                break
    visited, visiting = set(), set()
    result: List[str] = []
    def dfs(c: str) -> bool:
        if c in visiting:
            return False
        if c in visited:
            return True
        visiting.add(c)
        for dependent in adj[c]:
            if not dfs(dependent):
                return False
        visiting.remove(c)
        visited.add(c)
        result.append(c)
        return True
    for c in adj:
        if not dfs(c):
            return ''
    return ''.join(reversed(result))
