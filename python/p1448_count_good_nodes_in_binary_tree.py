from leetcode_utils import TreeNode

def count_good_nodes_nonlocal(root: TreeNode) -> int:
    count = 0
    def dfs(node: TreeNode, max_val: int):
        if not node:
            return
        nonlocal count
        if node.val >= max_val:
            count += 1
            max_val = node.val
        dfs(node.left, max_val)
        dfs(node.right, max_val)
    dfs(root, -10001)
    return count

def count_good_nodes(root: TreeNode) -> int:
    def dfs(node: TreeNode, max_val: int) -> int:
        if not node:
            return 0
        if node.val >= max_val:
            is_good = 1
            max_val = node.val
        else:
            is_good = 0
        return is_good + dfs(node.left, max_val) + dfs(node.right, max_val)
    return dfs(root, root.val)
