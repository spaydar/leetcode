from leetcode_utils import TreeNode
from typing import Optional

def invert_binary_tree_iterative(root: Optional[TreeNode]) -> Optional[TreeNode]:
    stack = list()
    if root:
        stack.append(root)
    while stack:
        curr = stack.pop()
        tmp = curr.left
        curr.left = curr.right
        curr.right = tmp
        if curr.left:
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)
    return root

def invert_binary_tree_recursive(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return root
    tmp = root.left
    root.left = root.right
    root.right = tmp
    invert_binary_tree_recursive(root.left)
    invert_binary_tree_recursive(root.right)
    return root
