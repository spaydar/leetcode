from typing import List

def find_order(num_courses: int, prerequisites: List[List[int]]) -> List[int]:
    from collections import defaultdict
    result, prereqs_dict, visiting, visited = [], defaultdict(list), set(), set()
    [prereqs_dict[dependent].append(dependency) for dependent, dependency in prerequisites]
    def dfs(course: int) -> bool:
        if course in visiting:
            return False
        if course in visited:
            return True
        visiting.add(course)
        for dependency in prereqs_dict[course]:
            if not dfs(dependency):
                return False
        visiting.remove(course)
        result.append(course)
        visited.add(course)
        return True
    for course in range(num_courses):
        if not dfs(course):
            return []
    return result
