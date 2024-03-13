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
    def merge_two_lists(a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode()
        while a and b:
            if a.val < b.val:
                cur.next = a
                a = a.next
            else:
                cur.next = b
                b = b.next
            cur = cur.next
        if a:
            cur.next = a
        if b:
            cur.next = b
        return dummy.next
    def mergesort(start: int, end: int) -> Optional[ListNode]:
        if start > end:
            return None
        if start == end:
            return lists[start]
        if start + 1 == end:
            return merge_two_lists(lists[start], lists[end])
        mid = start + (end - start) // 2
        left = mergesort(start, mid)
        right = mergesort(mid + 1, end)
        return merge_two_lists(left, right)
    return mergesort(0, len(lists) - 1)
