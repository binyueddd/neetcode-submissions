from functools import lru_cache

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, price in flights:
            graph[u].append((v, price))

        max_edges = k + 1

        @lru_cache(None)
        def dfs(airport, edges_left):
            # 从 airport 出发，还能坐 edges_left 段航班，到达 dst 的最低额外价格是多少？
            
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