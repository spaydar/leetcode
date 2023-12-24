from leetcode_utils import TreeNode
from typing import List, Optional

def binary_tree_right_side_view_bfs(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    result_list = []
    queue = [root]
    while queue:
        result_list.append(queue[-1].val)
        for _ in range(len(queue)):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return result_list

def binary_tree_right_side_view_dfs(root: Optional[TreeNode]) -> List[int]:
    result_list = []
    def dfs(node, depth):
        if not node:
            return
        if depth == len(result_list):
            result_list.append(node.val)
        dfs(node.right, depth + 1)
        dfs(node.left, depth + 1)
    dfs(root, 0)
    return result_list
