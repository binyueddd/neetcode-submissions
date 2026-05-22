class Solution:
    def isValid(self, s: str) -> bool:
        pairs={
            ")":"(",
            "}":"{",
            "]":"["
        }

        if not s:
            return False
        
        seen=[]

        for ch in s:
            if ch in pairs:
                if not seen or seen[-1]!=pairs[ch]:
                    return False
                
                seen.pop()
            else:
                seen.append(ch)
        return len(seen)==0
            
