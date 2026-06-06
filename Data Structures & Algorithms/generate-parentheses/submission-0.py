class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        m=2*n
        path=[]
        res=[]

        def dfs(i,left_count):
            if len(path)==m:
                res.append("".join(path)) #易错3
                return
            
            if left_count<n:
                path.append("(")
                dfs(i+1,left_count+1)
                path.pop()
            
            if i-left_count<left_count:
                path.append(")")
                dfs(i+1,left_count)
                path.pop()
            
        dfs(0,0)
        return res