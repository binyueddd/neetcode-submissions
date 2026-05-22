class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m=len(matrix)
        n=len(matrix[0])
        MARK = "#"
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    for k in range(n):
                        if matrix[i][k]!=0:
                            matrix[i][k]=MARK
                    for k in range(m):
                        if matrix[k][j]!=0:
                            matrix[k][j]=MARK

        for i in range(m):
            for j in range(n):
                if matrix[i][j]==MARK:
                    matrix[i][j]=0


        