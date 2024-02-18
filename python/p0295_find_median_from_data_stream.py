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
        pass

    def add_num(self, num: int) -> None:
        pass

    def find_median(self) -> float:
        return 0.0
