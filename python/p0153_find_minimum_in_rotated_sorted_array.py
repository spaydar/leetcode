from typing import List

def find_min(nums: List[int]) -> int:
    result = nums[0]
    l, r = 0, len(nums) - 1
    while l <= r:
        if nums[l] < nums[r]:
            result = min(result, nums[l])
            break
        m = l + (r - l) // 2
        result = min(result, nums[m])
        if nums[r] < nums[m]:
            l = m + 1
        else:
            r = m - 1
    return result

def find_min_no_extra_vars(nums: List[int]) -> int:
    l, r = 0, len(nums) - 1
    while nums[l] > nums[r]:
        m = l + (r - l) // 2
        if nums[m] > nums[r]:
            l = m + 1
        else:
            r = m
    return nums[l]
