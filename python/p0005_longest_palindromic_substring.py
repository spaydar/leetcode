def longest_palindromic_substring(s: str) -> str:
    result = ''
    def find_largest_palindrome(j: int, k: int):
        nonlocal result
        while j > -1 and k < len(s) and s[j] == s[k]:
            if k + 1 - j > len(result):
                result = s[j:k + 1]
            j -= 1
            k += 1
    for i in range(len(s)):
        find_largest_palindrome(i, i)
        find_largest_palindrome(i, i + 1)
    return result
