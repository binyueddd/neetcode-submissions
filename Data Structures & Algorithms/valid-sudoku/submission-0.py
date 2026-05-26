class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=defaultdict(set)
        col=defaultdict(set)
        block=defaultdict(set)

        for i in range(9):
            for j in range(9):
                cur=board[i][j]
                if cur==".":
                    continue
                
                block_id=(i//3)*3+(j//3)

                if cur in row[i]:
                    return False
                
                if cur in col[j]:
                    return False
                
                if cur in block[block_id]:
                    return False

                row[i].add(cur)
                col[j].add(cur)
                block[block_id].add(cur)
        
        return True
