from typing import Dict, Optional

class DoublyLinkedList:
    def __init__(self, key=0, val=0, next=None, prev=None) -> None:
        self.key: int = key
        self.val: int = val
        self.next: Optional[DoublyLinkedList] = next
        self.prev: Optional[DoublyLinkedList] = prev

class LRUCache:
    
    def __init__(self, capacity: int) -> None:
        self.capacity: int = capacity
        self.head: Optional[DoublyLinkedList] = None
        self.tail: Optional[DoublyLinkedList] = None
        self.key_vals: Dict[int, DoublyLinkedList] = {}

    def _move_node_to_head(self, node: DoublyLinkedList) -> None:
        # TODO move all logic related to moving link and self.tail to this fn (if possible)
        node.next = self.head
        node.prev = None
        self.head.prev = node
        self.head = node

    def get(self, key: int) -> int:
        if key not in self.key_vals:
            return -1
        node = self.key_vals[key]
        if node is not self.head:
            if node.prev and node.next:
                # remove link from current position
                node.prev.next = node.next
                node.next.prev = node.prev
            elif node is self.tail:
                # remove link from tail
                node.prev.next = None
                self.tail = node.prev
            # move to link to head
            self._move_node_to_head(node)
        return self.key_vals[key].val

    def put(self, key: int, value: int) -> None:
        if not self.key_vals:
            self.head = self.tail = DoublyLinkedList(key, value)
            self.key_vals[key] = self.head
            return
        if key in self.key_vals:
            node = self.key_vals[key]
            node.val = value
            self._move_node_to_head(node)
            return
        if len(self.key_vals) == self.capacity:
            del self.key_vals[self.tail.key]
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next.prev = None
                self.tail.next = None
        node = DoublyLinkedList(key, value)
        self.key_vals[key] = node
        self._move_node_to_head(node)
