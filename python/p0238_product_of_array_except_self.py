from typing import List

def product_except_self(nums: List[int]) -> List[int]:
    result = [1 for _ in nums]
    curr = 1
    for i in range(1, len(nums)):
        curr *= nums[i - 1]
        result[i] = curr
    curr = 1
    for i in range(len(nums) - 2, -1, -1):
        curr *= nums[i + 1]
        result[i] *= curr
    return result
