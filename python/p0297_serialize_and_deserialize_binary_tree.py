from leetcode_utils import TreeNode
from typing import List, Optional

def serialize(root: Optional[TreeNode]) -> str:
    lst = []
    def dfs(node: Optional[TreeNode]):
        if not node:
            lst.append('N')
            return
        lst.append(str(node.val))
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return ','.join(lst)

def deserialize(data: str) -> Optional[TreeNode]:
    lst = data.split(',')
    def dfs(vals: List[str]) -> Optional[TreeNode]:
        char = vals.pop(0)
        if char == 'N':
            return None
        node = TreeNode(int(char))
        node.left = dfs(vals)
        node.right = dfs(vals)
        return node
    root = dfs(lst)
    return root
