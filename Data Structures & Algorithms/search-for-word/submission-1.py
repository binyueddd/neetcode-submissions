class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        direction=[(0,1),(1,0),(-1,0),(0,-1)]
        m,n=len(board),len(board[0])

        def dfs(r,c,i):
            if board[r][c]!=word[i]:
                return False
            
            if i==len(word)-1:
                return True
            
            cur=board[r][c]
            board[r][c]="#"
            for x,y in direction:
                if 0<=r+x<m and 0<=c+y<n and dfs(r+x,c+y,i+1):
                    return True
            board[r][c]=cur

            return False
        
        for i in range(m):
            for j in range(n):
                if dfs(i,j,0):
                    return True
        return False


