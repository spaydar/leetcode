from heapq import heapify, heappop, heappush
from itertools import count
from leetcode_utils import ListNode
from typing import List, Optional

def merge_k_lists_heap(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    dummy = curr = ListNode(-1)
    counter = count()
    heap = [(node.val, -1 * next(counter), node) for node in lists if node]
    heapify(heap)
    while len(heap) > 1:
        _, _, node = heappop(heap)
        curr.next = node
        curr = curr.next
        if node.next:
            heappush(heap, (node.next.val, -1 * next(counter), node.next))
    if heap:
        curr.next = heap[0][2]
    return dummy.next

def merge_k_lists_mergesort(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    # TODO
    pass
