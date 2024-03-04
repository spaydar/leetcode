from math import ceil
from typing import List

def min_eating_speed(piles: List[int], h: int) -> int:
    l, r = 1, max(piles)
    result = r
    while l <= r:
        rate = l + (r - l) // 2
        hours = 0
        for pile in piles:
            hours += ceil(pile / rate)
        if hours <= h:
            result = min(result, rate)
            r = rate - 1
        else:
            l = rate + 1
    return result

def min_eating_speed_no_extra_var(piles: List[int], h: int) -> int:
    l, r = 1, max(piles)
    while l <= r:
        rate = l + (r - l) // 2
        hours = 0
        for pile in piles:
            hours += ceil(pile / rate)
        if hours <= h:
            r = rate - 1
        else:
            l = rate + 1
    return l
