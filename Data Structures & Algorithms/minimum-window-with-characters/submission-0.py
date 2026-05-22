class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window=defaultdict(int)
        need = Counter(t)
        required = len(need)
        meet_required = 0 #当前窗口已满足的字符种类

        if len(s)<len(t) or not s or not t:
            return ""
        
        start=0
        min_length=float('inf')
        window_start= 0
        for end in range(len(s)):
            ch = s[end]
            window[ch]+=1
            if ch in need and need[ch]==window[ch]:
                meet_required += 1
            
            while meet_required == required:
                window_length = end-start+1
                if window_length<min_length:
                    min_length = window_length
                    window_start=start

                window[s[start]]-=1

                if s[start] in need and window[s[start]]<need[s[start]]:
                    meet_required-=1
                
                start+=1

        if min_length==float('inf'):
            return ""

        return s[window_start:window_start+min_length]
        
