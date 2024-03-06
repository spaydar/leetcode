from typing import List

def find_median_of_two_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    NEG_INF, POS_INF = -1000001, 1000001
    A, B = nums1, nums2
    if len(A) > len(B):
        A, B = B, A
    total_len = len(A) + len(B)
    half_len = total_len // 2
    l, r = 0, len(A) - 1
    while True:
        mid_a = l + (r - l) // 2
        mid_b = half_len - mid_a - 2
        a_left = A[mid_a] if mid_a > -1 else NEG_INF
        a_right = A[mid_a + 1] if mid_a < len(A) - 1 else POS_INF
        b_left = B[mid_b] if mid_b > -1 else NEG_INF
        b_right = B[mid_b + 1] if mid_b < len(B) - 1 else POS_INF
        if a_left <= b_right and b_left <= a_right:
            if total_len % 2 == 0:
                return (max(a_left, b_left) + min(a_right, b_right)) / 2
            return min(a_right, b_right) * 1.0
        if a_left > b_right:
            r = mid_a - 1
        else:
            l = mid_a + 1
