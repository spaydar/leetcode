from typing import List

def trap_linear_memory(height: List[int]) -> int:
    # TODO this isn't working yet
    max_left_heights, max_right_heights = [0 for _ in range(len(height) + 2)], [0 for _ in range(len(height) + 2)]
    i = 1
    while i < len(height) + 1:
        max_left_heights[i] = max(height[i - 1], max_left_heights[i - 1])
        i += 1
    for i in range(len(height) - 1, -1, -1):
        max_right_heights[i + 1] = max(height[i], max_right_heights[i + 2])
    return -1

def trap_constant_memory(height: List[int]) -> int:
    return -1
