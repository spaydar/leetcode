import heapq
from typing import List

class KthLargest:
    def __init__(self, k: int, nums: List[int]) -> None:
        self.min_heap, self.k = nums, k
        heapq.heapify(self.min_heap)
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        if len(self.min_heap) >= self.k:
            heapq.heappushpop(self.min_heap, val)
        else:
            heapq.heappush(self.min_heap, val)
        return self.min_heap[0]
