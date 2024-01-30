def count_substrings(s: str) -> int:
    result = 0
    def find_palindromes(a: int, b: int) -> int:
        num_palindromes = 0
        while a > -1 and b < len(s) and s[a] == s[b]:
            num_palindromes += 1
            a -= 1
            b += 1
        return num_palindromes
    for i in range(len(s)):
        result += find_palindromes(i, i)
        result += find_palindromes(i, i + 1)
    return result
