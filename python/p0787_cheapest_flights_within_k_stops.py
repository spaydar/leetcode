from collections import defaultdict, deque
from typing import List

def find_cheapest_price_bellman_ford(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    MAX_INT = 1000001
    prev_prices = [MAX_INT for _ in range(n)]
    prev_prices[src] = 0
    for _ in range(k + 1):
        new_prices = prev_prices[:]
        for start, end, price in flights:
            if prev_prices[start] == MAX_INT:
                continue
            if prev_prices[start] + price < new_prices[end]:
                new_prices[end] = prev_prices[start] + price
        for i, price in enumerate(new_prices):
            prev_prices[i] = price
    return prev_prices[dst] if prev_prices[dst] < MAX_INT else -1

def find_cheapest_price_bfs(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    MAX_INT = 1000001
    prices = [MAX_INT for _ in range(n)]
    prices[src] = 0
    adj = defaultdict(list)
    for start, end, price in flights:
        adj[start].append((end, price))
    queue = deque([(0, src)])
    for _ in range(k + 1):
        for _ in range(len(queue)):
            total_cost, cur = queue.popleft()
            for nei, cost in adj[cur]:
                if total_cost + cost < prices[nei]:
                    prices[nei] = total_cost + cost
                    queue.append((total_cost + cost, nei))
    return prices[dst] if prices[dst] < MAX_INT else -1
