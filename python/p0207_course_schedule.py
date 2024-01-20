from typing import List

def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    from collections import defaultdict
    prereqs_dict, visiting = defaultdict(list), set()
    [prereqs_dict[dependent].append(dependency) for dependent, dependency in prerequisites]
    def dfs(course: int) -> bool:
        if course in visiting:
            return False
        if not prereqs_dict[course]:
            return True
        visiting.add(course)
        for dependency in prereqs_dict[course]:
            if not dfs(dependency):
                return False
        prereqs_dict[course] = []
        visiting.remove(course)
        return True
    for course in range(num_courses):
        if not dfs(course):
            return False
    return True
