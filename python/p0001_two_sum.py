from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    value_indices_dict = {}
    for i, val in enumerate(nums):
        diff = target - val
        if diff in value_indices_dict:
            return [value_indices_dict[diff], i]
        value_indices_dict[val] = i
    return [-1, -1]
