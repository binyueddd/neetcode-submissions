class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]

        for num in range(n+1):
            count=0
            x=num
            while x:
                count+=x&1
                x>>=1
            res.append(count)
        
        return res