from heapq import heappop, heappush, heappushpop
from typing import List

class MedianFinderBinarySearch:

    def __init__(self) -> None:
        self.nums: List[int] = []

    def add_num(self, num: int) -> None:
        l, r = 0, len(self.nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if self.nums[m] == num:
                self.nums.insert(m, num)
                return
            elif self.nums[m] < num:
                l = m + 1
            else:
                r = m - 1
        self.nums.insert(l, num)

    def find_median(self) -> float:
        n = len(self.nums)
        half = n // 2
        if n % 2 == 1:
            return float(self.nums[half])
        return self.nums[half] + (self.nums[half - 1] - self.nums[half]) / 2

class MedianFinderHeap:

    def __init__(self) -> None:
        self.max_heap = [] # Smaller half stored in max heap
        self.min_heap = [] # Larger half stored in min heap

    def add_num(self, num: int) -> None:
        heappush(self.max_heap, num * -1)

        if self.min_heap and self.max_heap[0] * -1 > self.min_heap[0]:
            heappush(self.min_heap, heappop(self.max_heap) * -1)

        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, heappop(self.max_heap) * -1)
        elif len(self.min_heap) > len(self.max_heap) + 1:
            heappush(self.max_heap, heappop(self.min_heap) * -1)

    def find_median(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return self.max_heap[0] * -1
        if len(self.max_heap) < len(self.min_heap):
            return self.min_heap[0]
        return (self.max_heap[0] * -1 + self.min_heap[0]) / 2

class MedianFinderHeapPushPop:
    # heappushpop performs better than separate calls to heappush and heappop as per heapq docs
    def __init__(self) -> None:
        self.small = []
        self.large = []

    def add_num(self, num: int) -> None:
        if len(self.small) == len(self.large):
            heappush(self.small, heappushpop(self.large, num) * -1)
        else:
            heappush(self.large, heappushpop(self.small, num * -1) * -1)

    def find_median(self) -> float:
        if len(self.small) == len(self.large):
            return (self.large[0] - self.small[0]) / 2
        return self.small[0] * -1
