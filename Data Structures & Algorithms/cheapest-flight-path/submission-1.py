from collections import defaultdict
from functools import lru_cache
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, price in flights:
            graph[u].append((v, price))

        max_edges = k + 1

        @lru_cache(None)
        def dfs(airport, edges_left):
            if airport == dst:
                return 0

            if edges_left == 0:
                return float("inf")

            best = float("inf")

            for nei, price in graph[airport]:
                next_cost = dfs(nei, edges_left - 1)
                best = min(best, price + next_cost)

            return best

        ans = dfs(src, max_edges)

        return ans if ans != float("inf") else -1