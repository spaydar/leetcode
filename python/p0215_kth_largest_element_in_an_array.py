import heapq
from random import randint
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
    return -1

def find_kth_largest_quick_select(nums: List[int], k: int) -> int:
    # This times out on LeetCode for a particular large test case
    k = len(nums) - k
    def quick_select(l: int, r: int) -> int:
        i = l
        for j in range(l, r):
            if nums[j] <= nums[r]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[r] = nums[r], nums[i]
        if i > k:
            return quick_select(l, i - 1)
        if i < k:
            return quick_select(l + 1, r)
        return nums[i]
    return quick_select(0, len(nums) - 1)

def find_kth_largest_quick_select_random(nums: List[int], k: int) -> int:
    # This times out on LeetCode for a different large test case than above
    k = len(nums) - k
    def quick_select(l: int, r: int) -> int:
        i, pivot = l, randint(l, r)
        nums[pivot], nums[r] = nums[r], nums[pivot]
        for j in range(l, r):
            if nums[j] <= nums[r]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[r] = nums[r], nums[i]
        if i > k:
            return quick_select(l, i - 1)
        if i < k:
            return quick_select(l + 1, r)
        return nums[i]
    return quick_select(0, len(nums) - 1)
