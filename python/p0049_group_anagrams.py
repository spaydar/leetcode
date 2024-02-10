from collections import defaultdict
from typing import List

def group_anagrams(strs: List[str]) -> List[List[str]]:
    char_count_dict = defaultdict(list)
    for s in strs:
        char_counts = [0 for _ in range(26)]
        for c in s:
            char_counts[ord(c) - ord('a')] += 1
        char_count_dict[tuple(char_counts)].append(s)
    return list(char_count_dict.values())
