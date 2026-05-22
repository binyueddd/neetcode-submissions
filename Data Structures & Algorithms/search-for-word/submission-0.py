class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        direction=[(0,1),(0,-1),(1,0),(-1,0)]
        row, col = len(board),len(board[0])
        def backtracking(r,c,i):
            if r<0 or r>=row or c<0 or c>=col:
                return False
            
            if board[r][c]!=word[i]:
                return False
            
            if i==len(word)-1:
                return True
            
            visited=board[r][c]
            board[r][c]="#"

            for dir_row,dir_col in direction:
                if backtracking(r+dir_row,c+dir_col,i+1):
                    board[r][c]=visited
                    return True
            
            board[r][c]=visited
            return False

        for i in range(row):
            for j in range(col):
                if backtracking(i,j,0):
                    return True
        return False

            
