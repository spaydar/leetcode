from typing import List

def encode(strs: List[str]) -> str:
    result = []
    for s in strs:
        result.append(str(len(s)) + '|')
        result.append(s)
    return ''.join(result)

def decode(s: str) -> List[str]:
    result = []
    start = 0
    while start < len(s):
        end = start
        while s[end] != '|':
            end += 1
        str_len = int(s[start:end])
        result.append(s[end + 1: end + 1 + str_len])
        start = end + 1 + str_len
    return result
