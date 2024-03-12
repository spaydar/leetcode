from collections import OrderedDict
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
        if node is self.head:
            return
        if node.prev and node.next:
            # remove link from current position
            node.prev.next = node.next
            node.next.prev = node.prev
        elif node is self.tail:
            # remove link from tail
            node.prev.next = None
            self.tail = node.prev
        node.next = self.head
        node.prev = None
        self.head.prev = node
        self.head = node

    def get(self, key: int) -> int:
        if key not in self.key_vals:
            return -1
        node = self.key_vals[key]
        self._move_node_to_head(node)
        return node.val

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
        if not self.tail:
            self.tail = node

class LRUCacheDummyNodes:

    def __init__(self, capacity: int) -> None:
        self.capacity: int = capacity
        self.cache: Dict[int, DoublyLinkedList] = {}
        self.head: DoublyLinkedList = DoublyLinkedList(-1, -1)
        self.tail: DoublyLinkedList = DoublyLinkedList(-1, -1)
        self.head.next, self.tail.prev = self.tail, self.head

    def _insert(self, node: DoublyLinkedList) -> None:
        nxt = self.head.next
        self.head.next = nxt.prev = node
        node.prev, node.next = self.head, nxt

    def _remove(self, node: DoublyLinkedList) -> None:
        prv, nxt = node.prev, node.next
        prv.next, nxt.prev = nxt, prv

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        if self.head.next is not node:
            self._remove(node)
            self._insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
        else:
            node = DoublyLinkedList(key, value)
            self.cache[key] = node
        self._insert(node)
        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]

class LRUCacheOrderedDict:

    def __init__(self, capacity: int) -> None:
        self.capacity: int = capacity
        self.cache: OrderedDict = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key, last=False)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key, last=False)
        if len(self.cache) > self.capacity:
            self.cache.popitem()
