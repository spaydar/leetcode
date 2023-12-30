from leetcode_utils import TreeNode
from typing import Optional

def serialize(root: Optional[TreeNode]) -> str:
    lst = []
    def dfs(node: Optional[TreeNode]):
        if not node:
            lst.append('N')
            return
        lst.append(node.val)
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return ','.join(lst)

def deserialize(data: str) -> Optional[TreeNode]:
    lst = str.split(',')
    char = lst.pop(0)
    root = None if char == 'N' else TreeNode(int(char))
    def dfs(node: Optional[TreeNode]):
        # TODO it might be easier to implement this with a TreeNode return type
        if not lst:
            return
        char = lst.pop(0)
        if char != 'N':
            node.left = TreeNode(int(char))
            dfs(node.left)
        else:
            node.left = 
    return root
