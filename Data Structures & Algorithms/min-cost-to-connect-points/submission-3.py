class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        heap=[(0,0)] #cost,index
        visited=set() #已经进入 MST 的节点集合
        res = 0

        while len(visited)<n:
            cost, idx = heapq.heappop(heap)

            if idx in visited: 
                continue

            visited.add(idx)
            res+=cost

            x1,y1 = points[idx]

            for i in range(n):
                if i in visited:
                    continue
                
                x2,y2 = points[i]
                dist = abs(x1-x2)+abs(y1-y2)
                heapq.heappush(heap,(dist,i))
        
        return res