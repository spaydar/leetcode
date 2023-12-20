from leetcode_utils import TreeNode
from typing import Optional, Tuple

def diameter_of_binary_tree(root: Optional[TreeNode]) -> int:
    diameter = 0
    def helper(node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        left = helper(node.left)
        right = helper(node.right)
        nonlocal diameter
        diameter = max(diameter, left + right)
        return 1 + max(left, right)
    helper(root)
    return diameter
