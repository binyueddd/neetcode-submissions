class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=defaultdict(list)

        for cur,prev in prerequisites:
            graph[prev].append(cur)
        
        state = [0] * numCourses

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
