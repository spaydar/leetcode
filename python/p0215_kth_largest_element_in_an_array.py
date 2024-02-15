import heapq
from typing import List

def find_kth_largest_min_heap(nums: List[int], k: int) -> int:
    heapq.heapify(nums)
    target, result = len(nums) - k, -1
    while target > -1:
        result = heapq.heappop(nums)
        target -= 1
    return result

def find_kth_largest_max_heap(nums: List[int], k: int) -> int:
    # TODO

def find_kth_largest_quick_select(nums: List[int], k: int) -> int:
    # TODO
