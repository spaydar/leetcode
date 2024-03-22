from typing import List

def two_sum(numbers: List[int], target: int) -> List[int]:
    left, right = 0, len(numbers) - 1
    while True:
        val = numbers[left] + numbers[right]
        if val == target:
            return [left + 1, right + 1]
        if val < target:
            left += 1
        else:
            right -= 1

def two_sum_simplified(numbers: List[int], target: int) -> List[int]:
    left, right = 0, len(numbers) - 1
    while numbers[left] + numbers[right] != target:
        if numbers[left] + numbers[right] < target:
            left += 1
        else:
            right -= 1
    return [left + 1, right + 1]
