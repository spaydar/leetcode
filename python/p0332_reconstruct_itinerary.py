from collections import defaultdict
from typing import List

def find_itinerary_recursive_intuitive(tickets: List[List[str]]) -> List[str]:
    # This times out for large input on LeetCode - test case 80
    tickets.sort(reverse=True)
    adj = defaultdict(list)
    for src, dest in tickets:
        adj[src].append(dest)
    result = ['JFK']
    def dfs(src: str) -> bool:
        if len(result) == len(tickets) + 1:
            return True
        if src not in adj or not adj[src]:
            return False
        for i in reversed(range(len(adj[src]))):
            if adj[src][i] == '*':
                continue
            dest = adj[src][i]
            adj[src][i] = '*'
            result.append(dest)
            if dfs(dest):
                return True
            result.pop()
            adj[src][i] = dest
        return False
    dfs('JFK')
    return result

def find_itinerary_recursive_optimal(tickets: List[List[str]]) -> List[str]:
    # https://leetcode.com/problems/reconstruct-itinerary/solutions/78768/short-ruby-python-java-c/
    adj = defaultdict(list)
    for src, dest in sorted(tickets, reverse=True):
        adj[src].append(dest)
    result = []
    def dfs(src: str):
        while adj[src]:
            dfs(adj[src].pop())
        result.append(src)
    dfs('JFK')
    return result[::-1]

def find_itinerary_iterative_optimal(tickets: List[List[str]]) -> List[str]:
    # https://leetcode.com/problems/reconstruct-itinerary/solutions/78768/short-ruby-python-java-c/
    adj = defaultdict(list)
    for src, dest in sorted(tickets, reverse=True):
        adj[src].append(dest)
    result, stack = [], ['JFK']
    while stack:
        while adj[stack[-1]]:
            stack.append(adj[stack[-1]].pop())
        result.append(stack.pop())
    return result[::-1]
