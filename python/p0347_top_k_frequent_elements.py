from collections import defaultdict
from typing import List

def top_k_frequent(nums: List[int], k: int) -> List[int]:
    occurrence_counts_dict = defaultdict(int)
    for n in nums:
        occurrence_counts_dict[n] += 1
    occurrence_buckets = [[] for _ in nums]
    for key, val in occurrence_counts_dict.items():
        occurrence_buckets[val - 1].append(key)
    result = []
    for lst in reversed(occurrence_buckets):
        result.extend(lst)
        if len(result) == k:
            break
    return result
