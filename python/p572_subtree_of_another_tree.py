from leetcode_utils import TreeNode
from typing import Optional

def is_subtree(root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
    def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None or p.val != q.val:
            return False
        return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
    if sub_root is None:
        return True
    if root is None:
        return False
    if is_same_tree(root, sub_root):
        return True
    return is_subtree(root.left, sub_root) or is_subtree(root.right, sub_root)
