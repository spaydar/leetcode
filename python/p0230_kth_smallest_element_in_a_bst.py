from leetcode_utils import TreeNode
from typing import Optional, Tuple

def kth_smallest_recursive(root: Optional[TreeNode], k: int) -> int:
    def dfs(node: Optional[TreeNode], val, count) -> Tuple[int, int]:
        # Optionally can add `or count == k` to reduce number of nodes traversed -- whether this outweighs the overhead depends on the tree
        if not node:
            return val, count
        val, count = dfs(node.left, val, count)
        if count == k:
            return val, count
        return dfs(node.right, node.val, count + 1)
    return dfs(root, -1, 0)[0]

def kth_smallest_iterative(root: Optional[TreeNode], k: int) -> int:
    pass
