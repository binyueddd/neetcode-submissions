class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m=len(board)
        n=len(board[0])
        directions=[(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(r,c):
            if r<0 or r>=m or c<0 or c>=n or board[r][c]!='O':
                return

            board[r][c]="#"
            for dx, dy in directions:
                x,y=r+dx,c+dy
                dfs(x,y)

        for row in range(m):
            dfs(row,0)
            dfs(row,n-1)
        
        for col in range(n):
            dfs(0,col)
            dfs(m-1,col)
        
        for i in range(m):
            for j in range(n):
                if board[i][j]=="O":
                    board[i][j]='X'
                if board[i][j]=='#':
                    board[i][j]='O'