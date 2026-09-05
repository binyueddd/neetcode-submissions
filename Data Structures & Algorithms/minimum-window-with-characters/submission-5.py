class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or len(s)<len(t):
            return ""

        need = Counter(t)
        window = defaultdict(int)
        have = 0
        need_count = len(need)

        left=0
        res_left=0
        min_len = float('inf')

        for right in range(len(s)):
            ch = s[right]
            window[ch]+=1

            if ch in need and need[ch]==window[ch]:
                have+=1

            while have == need_count:
                if right-left+1<min_len:
                    min_len = right-left+1
                    res_left=left
                
                left_ch = s[left]
                window[left_ch]-=1

                if need[left_ch] > window[left_ch]:
                    have-=1
                
                left+=1
        
        if min_len==float('inf'):
            return ""
        
        else:
            return s[res_left:res_left+min_len]


