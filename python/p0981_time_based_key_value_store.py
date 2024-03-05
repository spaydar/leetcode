from collections import defaultdict
from typing import DefaultDict, List, Tuple

class TimeMap:

    def __init__(self) -> None:
        self.data: DefaultDict[str, List[Tuple[int, str]]] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.data or self.data[key][0][0] > timestamp:
            return ''
        l, r = 0, len(self.data[key]) - 1
        while l <= r:
            m = l + (r - l) // 2
            if self.data[key][m][0] == timestamp:
                return self.data[key][m][1]
            if self.data[key][m][0] < timestamp:
                l = m + 1
            else:
                r = m - 1
        return self.data[key][r][1]

    def get_optimized(self, key: str, timestamp: int) -> str:
        if not key in self.data or self.data[key][0][0] > timestamp:
            return ''
        # Checking the last element before searching is not necessary but provides significat improvement on LeetCode
        if self.data[key][-1][0] <= timestamp:
            return self.data[key][-1][1]
        l, r = 0, len(self.data[key]) - 1
        while l <= r:
            m = l + (r - l) // 2
            if self.data[key][m][0] == timestamp:
                return self.data[key][m][1]
            if self.data[key][m][0] < timestamp:
                l = m + 1
            else:
                r = m - 1
        return self.data[key][r][1]
