def is_anagram_array(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    chars = [0 for _ in range(26)]
    for i in range(len(s)):
        chars[ord(s[i]) - 97] += 1
        chars[ord(t[i]) - 97] -= 1
    for c in chars:
        if c != 0:
            return False
    return True

def is_anagram_sort(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    s_chars = sorted(s)
    t_chars = sorted(t)
    for i in range(len(s)):
        if s_chars[i] != t_chars[i]:
            return False
    return True
