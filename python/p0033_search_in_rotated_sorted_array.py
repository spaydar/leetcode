from typing import List

def search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        m = l + (r - l) // 2
        if nums[m] == target:
            return m
        if nums[m] > nums[r]:
            if nums[m] < target or nums[l] > target:
                l = m + 1
            else:
                r = m - 1
        else:
            if nums[m] > target or nums[r] < target:
                r = m - 1
            else:
                l = m + 1
    return -1

def search_intuitive_if_conds(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        m = l + (r - l) // 2
        if nums[m] == target:
            return m
        if nums[m] > nums[r]:
            if nums[l] <= target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        else:
            if nums[m] < target <= nums[r]:
                l = m + 1
            else:
                r = m - 1
    return -1
