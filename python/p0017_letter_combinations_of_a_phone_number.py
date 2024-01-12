from typing import List

def letter_combinations(digits: str) -> List[str]:
    if not digits:
        return []
    result = []
    digit_chars_dict = {
        '2': ('a','b','c'),
        '3': ('d','e','f'),
        '4': ('g','h','i'),
        '5': ('j','k','l'),
        '6': ('m','n','o'),
        '7': ('p','q','r','s'),
        '8': ('t','u','v'),
        '9': ('w','x','y','z')
    }
    curr = []
    def dfs(i: int):
        if i == len(digits):
            result.append(''.join(curr))
            return
        for c in digit_chars_dict[digits[i]]:
            curr.append(c)
            dfs(i + 1)
            curr.pop()
    dfs(0)
    return result
