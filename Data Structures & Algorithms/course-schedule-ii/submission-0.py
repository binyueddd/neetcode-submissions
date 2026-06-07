class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        indegree=[0]*numCourses
        for cur, prev in prerequisites:
            graph[prev].append(cur)
            indegree[cur]+=1
        
        queue=deque()
        for course in range(numCourses):
            if indegree[course]==0:
                queue.append(course)

        order=[]
        while queue:
            course=queue.popleft()
            order.append(course)

            for nxt_course in graph[course]:
                
                indegree[nxt_course]-=1
                if indegree[nxt_course]==0:
                    queue.append(nxt_course)
                
        if len(order)==numCourses:
            return order
        return []

