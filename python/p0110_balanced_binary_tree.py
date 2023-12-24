from leetcode_utils import TreeNode
from typing import Optional, Tuple

def balanced_binary_tree(root: Optional[TreeNode]) -> bool:
    def helper(node: Optional[TreeNode]) -> Tuple[bool, int]:
        if not node:
            return True, 0
        left_balanced, left_height = helper(node.left)
        if not left_balanced:
            return False, 0
        right_balanced, right_height = helper(node.right)
        if not right_balanced:
            return False, 0
        if abs(left_height - right_height) > 1:
            return False, 0
        return True, max(left_height, right_height) + 1
    return helper(root)[0]
