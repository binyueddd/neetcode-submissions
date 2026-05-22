class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph=defaultdict(list)
        for a,b in prerequisites:
            graph[b].append(a)
        
        state=[0]*numCourses
        #state:0 not visited; 1: visited; 2: visited and safe
        def dfs(course):
            if state[course]==1:
                return False
            if state[course]==2:
                return True
            
            state[course]=1
            for nxt in graph[course]:
                if not dfs(nxt):
                    return False
                
            state[course]=2
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True