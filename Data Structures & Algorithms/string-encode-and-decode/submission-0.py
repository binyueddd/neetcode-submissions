class Solution:

    def encode(self, strs: List[str]) -> str:
        res=[]
        for string in strs:
            res.append(str(len(string)))
            res.append("#")
            
            res.append(string)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i=0
        while i<len(s):
            j=i
            while s[j] != "#":
                j+=1
            
            length = int(s[i:j])
            word_start = j+1
            word_end = j+length
            res.append(s[j+1:j+length+1])
            i=j+length+1
        return res
            