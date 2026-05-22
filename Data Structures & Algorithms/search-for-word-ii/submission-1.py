class TrieNode:
    def __init__(self):
        self.children = {}
        self.word=None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        row,col=len(board),len(board[0])
        root = TrieNode()
        
        for word in words:
            cur=root
            for ch in word:
                if ch not in cur.children:
                    cur.children[ch]=TrieNode()
                cur=cur.children[ch]
            cur.word=word
        
        res=[]

        def dfs(r,c,node):
            if r<0 or r>=row or c<0 or c>=col:
                return
            
            ch=board[r][c]
            

            if ch not in node.children:
                return
            
            if node.children[ch].word:
                res.append(node.children[ch].word)
                node.children[ch].word=None

            board[r][c]="#"
            for i,j in [(1,0),(0,1),(-1,0),(0,-1)]:
                dfs(r+i,c+j,node.children[ch])
            board[r][c]=ch

        for i in range(row):
            for j in range(col):
                dfs(i,j,root)
        return res