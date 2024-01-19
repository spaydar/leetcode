from typing import List

def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    prereqs_dict, visiting = {}, set()
    for dependent, dependency in prerequisites:
        if dependent in prereqs_dict:
            prereqs_dict[dependent].append(dependency)
        else:
            prereqs_dict[dependent] = [dependency]
    def dfs(course: int) -> bool:
        if course in visiting:
            return False
        if course not in prereqs_dict or not prereqs_dict[course]:
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
