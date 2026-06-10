class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last={}
        for i, ch in enumerate(s):
            last[ch]=i
        
        end=0
        res=[]
        start=0
        for i, ch in enumerate(s):
            end=max(end,last[ch])
            if end==i:
                res.append(end-start+1)
                start=end+1
        return res