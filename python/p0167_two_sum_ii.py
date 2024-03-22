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
