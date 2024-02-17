from collections import Counter, defaultdict, deque
import heapq
from typing import List

def least_interval_heap(tasks: List[str], n: int) -> int:
    num_occurrences = defaultdict(int)
    for t in tasks:
        num_occurrences[t] += 1
    max_heap = [v * -1 for v in num_occurrences.values()]
    heapq.heapify(max_heap)
    queue, time = deque(), 0
    while len(max_heap) > 0 or len(queue) > 0:
        if len(max_heap) > 0:
            curr = heapq.heappop(max_heap) + 1
            if curr < 0:
                queue.append((curr, time + n))
        if len(queue) > 0 and queue[0][1] <= time:
            heapq.heappush(max_heap, queue.popleft()[0])
        time += 1
    return time

def least_interval_slots(tasks: List[str], n: int) -> int:
    counts = Counter(tasks).values()
    max_freq = max(counts)
    max_freq_count = list(counts).count(max_freq)
    min_slots = (max_freq - 1) * (n + 1) + max_freq_count
    return max(min_slots, len(tasks))
