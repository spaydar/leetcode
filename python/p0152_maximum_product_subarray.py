from typing import List

def max_product_memo(nums: List[int]) -> int:
    result = nums[0]
    high, low = 1, 1
    for n in nums:
        tmp = high
        high = max(n * high, n * low, n)
        low = min(n * tmp, n * low, n)
        result = max(result, high)
    return result
