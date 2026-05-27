class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n=len(s)
        m=len(t)
        if n<m or not s or not t:
            return ""

        need = Counter(t)
        window=defaultdict(int)

        min_len=float('inf')
        start=0
        need_count=0
        ans_start=0

        for end in range(len(s)):
            ch=s[end]
            window[ch]+=1
            if ch in need and window[ch]==need[ch]:
                need_count+=1
            
            while need_count==len(need):
                window_len=end-start+1
                if window_len<min_len:
                    min_len=window_len
                    ans_start=start
                
                window[s[start]]-=1

                if s[start] in need and window[s[start]]<need[s[start]]:
                    need_count-=1
                start+=1
        
        if min_len==float('inf'):
            return ""
        
        return s[ans_start:ans_start+min_len]

                
