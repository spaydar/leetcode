import heapq
from typing import List

def last_stone_weight(stones: List[int]) -> int:
    neg_stones = [s * -1 for s in stones]
    heapq.heapify(neg_stones)
    while len(neg_stones) > 1:
        y = heapq.heappop(neg_stones) * -1
        x = neg_stones[0] * -1
        if y == x:
            heapq.heappop(neg_stones)
        else:
            heapq.heapreplace(neg_stones, (y - x) * -1)
    return neg_stones[0] * -1 if len(neg_stones) > 0 else 0

def last_stone_weight_mut(stones: List[int]) -> int:
    for i in range(len(stones)):
        stones[i] *= -1
    heapq.heapify(stones)
    while len(stones) > 1:
        y = heapq.heappop(stones)
        x = stones[0]
        if y == x:
            heapq.heappop(stones)
        else:
            heapq.heapreplace(stones, y - x)
    stones.append(0)
    return stones[0] * -1
