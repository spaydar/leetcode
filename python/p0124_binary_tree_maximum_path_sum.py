from leetcode_utils import TreeNode
from typing import Optional

def max_path_sum(root: TreeNode) -> int:
    result = root.val
    def dfs(node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        left_path_sum = dfs(node.left)
        right_path_sum = dfs(node.right)
        sum_two_branches = node.val + left_path_sum + right_path_sum
        sum_one_branch = node.val + max(left_path_sum, right_path_sum)
        nonlocal result
        result = max(result, sum_two_branches, sum_one_branch, node.val)
        return node.val + max(left_path_sum, right_path_sum, 0)
    dfs(root)
    return result

def max_path_sum_neetcode(root: TreeNode) -> int:
    result = root.val
    def dfs(node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        left_path_sum = max(dfs(node.left), 0)
        right_path_sum = max(dfs(node.right), 0)
        nonlocal result
        result = max(result, node.val + left_path_sum + right_path_sum)
        return node.val + max(left_path_sum, right_path_sum)
    dfs(root)
    return result
