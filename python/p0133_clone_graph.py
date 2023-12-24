from leetcode_utils import Node
from typing import Optional

def clone_graph(node: Optional[Node]) -> Optional[Node]:
    if not node:
        return None
    old_to_new = {}
    def dfs(node: Node) -> Node:
        if node in old_to_new:
            return old_to_new[node]
        new = Node(node.val)
        old_to_new[node] = new
        for n in node.neighbors:
            new.neighbors.append(dfs(n))
        return new
    return dfs(node)
