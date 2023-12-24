from leetcode_utils import TreeNode
from typing import Optional

def maximum_depth_of_binary_tree_recursive(root: Optional[TreeNode]) -> int:
    def helper(node: Optional[TreeNode], count: int) -> int:
        if not node:
            return count
        depth_left = helper(node.left, count + 1)
        depth_right = helper(node.right, count + 1)
        return max(depth_left, depth_right)
    return helper(root, 0) if root else 0

def maximum_depth_of_binary_tree_iterative_dfs(root: Optional[TreeNode]) -> int:
    stack = list()
    if root:
        stack.append((root, 0))
    max_depth = 0
    while stack:
        node, depth = stack.pop()
        if node:
            max_depth = max(max_depth, depth + 1)
            stack.append((node.left, depth + 1))
            stack.append((node.right, depth + 1))
    return max_depth

def maximum_depth_of_binary_tree_iterative_bfs(root: Optional[TreeNode]) -> int:
    queue = list()
    if root:
        queue.append(root)
    level = 0
    while (queue):
        level += 1
        for _ in range(len(queue)):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return level
