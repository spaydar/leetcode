from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def copy_random_list(head: Optional[Node]) -> Optional[Node]:
    node_map = { None: None }
    runner = head
    while runner:
        node_map[runner] = Node(runner.val)
        runner = runner.next
    runner = head
    while runner:
        new_node = node_map[runner]
        new_node.next = node_map[runner.next]
        new_node.random = node_map[runner.random]
        runner = runner.next
    return node_map[head]
