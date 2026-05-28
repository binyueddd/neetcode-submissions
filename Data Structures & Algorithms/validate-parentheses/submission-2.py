class Solution:
    def isValid(self, s: str) -> bool:
        pairs={
            "}":"{",
            ")":"(",
            "]":"["
        }

        cur=[]

        if not s:
            return False

        for ch in s:
            if ch in pairs:
                if not cur or cur[-1]!=pairs[ch]:
                    return False
                
                cur.pop()
            else:
                cur.append(ch)
        
        return len(cur)==0
