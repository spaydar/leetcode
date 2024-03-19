from typing import List

def longest_consecutive(nums: List[int]) -> int:
    longest = 0
    nums_set = set(nums)
    for n in nums:
        if n - 1 in nums_set:
            continue
        cur_len = 1
        while n + cur_len in nums_set:
            cur_len += 1
        longest = max(longest, cur_len)
    return longest

def longest_consecutive_mutate_set(nums: List[int]) -> int:
    longest = 0
    nums_set = set(nums)
    while longest < len(nums_set):
        n = nums_set.pop()
        hi = n
        while hi + 1 in nums_set:
            hi += 1
            nums_set.remove(hi)
        lo = n
        while lo - 1 in nums_set:
            lo -= 1
            nums_set.remove(lo)
        longest = max(longest, hi - lo + 1)
    return longest
