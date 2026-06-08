class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        visited=[False]*n

        min_dist=[float('inf')]*n
        min_dist[0]=0

        total_cost=0

        for _ in range(n):
            cur=-1
            cur_dist=float('inf')

            for i in range(n):
                if not visited[i] and min_dist[i]<cur_dist:
                    cur_dist=min_dist[i]
                    cur=i
            
            visited[cur] = True
            total_cost += cur_dist


            x1, y1 = points[cur]
            for nxt in range(n):
                if not visited[nxt]:
                    x2, y2 = points[nxt]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    min_dist[nxt] = min(min_dist[nxt], dist)

        return total_cost