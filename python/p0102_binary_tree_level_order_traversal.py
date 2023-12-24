from leetcode_utils import TreeNode
from typing import List, Optional

def binary_tree_level_order_traversal(root: Optional[TreeNode]) -> List[List[int]]:
    result_list = []
    if not root:
        return result_list
    queue = [root]
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.pop(0)
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result_list.append(level)
    return result_list
