class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s)<len(t):
            return ""
        
        need = Counter(t)
        best = ""
        for i in range(len(s)):
            window = defaultdict(int)
            for j in range(i, len(s)):
                window[s[j]]+=1

                valid=True #检查所有字符
                for ch in need:
                    if need[ch]>window[ch]:
                        valid=False
                        break
                if valid:
                    substring = s[i:j+1]
                    if best == "" or len(substring)<len(best):
                        best=substring
                    break
        return best