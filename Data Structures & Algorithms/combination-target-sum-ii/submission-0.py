class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        path=[]
        n=len(candidates)
        candidates.sort()
        def dfs(i,total):
            if total==target:
                res.append(path[:])
                return
            
            for j in range(i,n):
                if total+candidates[i]>target:
                    break
                
                if j>i and candidates[j]==candidates[j-1]:
                    continue
                
                path.append(candidates[j])
                dfs(j+1,candidates[j]+total)
                path.pop()
        
        dfs(0,0)
        return res