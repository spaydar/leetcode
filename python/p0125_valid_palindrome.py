from typing import List

def is_palindrome(s: str) -> bool:
    chars: List[str] = []
    for ch in s:
        if ch.isalnum():
            chars.append(ch.lower())
    mid, remainder = divmod(len(chars), 2)
    if remainder:
        left, right = mid, mid
    else:
        left, right = mid - 1, mid
    while left > -1 and right < len(chars):
        if chars[left] != chars[right]:
            return False
        left -= 1
        right += 1
    return True

def is_palindrome_constant_memory(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        else:
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
    return True
