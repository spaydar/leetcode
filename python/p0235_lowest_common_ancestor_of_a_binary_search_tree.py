from leetcode_utils import TreeNode

def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if root.val == p.val or root.val == q.val or p.val < root.val < q.val or q.val < root.val < p.val:
        return root
    if root.val > p.val:
        return lowest_common_ancestor(root.left, p, q)
    return lowest_common_ancestor(root.right, p, q)

def lowest_common_ancestor_iterative(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    while root:
        if root.val > p.val and root.val > q.val:
            root = root.left
        elif root.val < p.val and root.val < q.val:
            root = root.right
        else:
            return root
