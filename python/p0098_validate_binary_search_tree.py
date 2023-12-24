from leetcode_utils import TreeNode
from typing import Optional

def is_valid_bst(root: Optional[TreeNode]) -> bool:
    def dfs(node: TreeNode, min_val, max_val) -> bool:
        if not node:
            return True
        if not min_val < node.val < max_val:
            return False
        return dfs(node.left, min_val, node.val) and dfs(node.right, node.val, max_val)
    return dfs(root, float('-inf'), float('inf'))
