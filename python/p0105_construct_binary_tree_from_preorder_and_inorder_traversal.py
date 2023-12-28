from leetcode_utils import TreeNode
from typing import List, Optional

def build_tree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if not preorder:
        return None
    head = TreeNode(preorder[0])
    left_len = inorder.index(head.val)
    head.left = build_tree(preorder[1:1 + left_len], inorder[:left_len])
    head.right = build_tree(preorder[1 + left_len:], inorder[1 + left_len:])
    return head
