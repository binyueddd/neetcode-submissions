class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalin(s):
            left=0
            right=len(s)-1
            while left<right:
                if s[left]!=s[right]:
                    return False
                
                left+=1
                right-=1
            return True
        
        path=[]
        res=[]

        def dfs(i):
            if i==len(s):
                res.append(path[:])
            
            for j in range(i,len(s)):
                cur=s[i:j+1]
                if isPalin(cur):
                    path.append(cur)
                    dfs(j+1)
                    path.pop()
        
        dfs(0)
        return res
