from typing import List

def three_sum(nums: List[int]) -> List[List[int]]:
    # TODO this isn't working yet
    # consider case where a target number isn't found -- we shouldn't increment both pointers
    result = []
    nums.sort()
    def binary_search(start: int, end: int, target: int) -> int:
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                return mid
        return -1
    left, right = 0, len(nums) - 1
    while left < right:
        idx = binary_search(left + 1, right - 1, 0 - (nums[left] + nums[right]))
        if idx != -1:
            result.append([nums[left], nums[idx], nums[right]])
        left += 1
        right -= 1
        while (
                left < len(nums) and 
                right > -1 and
                nums[left] == nums[left - 1] and
                nums[right] == nums[right + 1]
        ):
            right -= 1
    return result
