class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found=[False,False,False]
        x,y,z=target
        for a,b,c in triplets:
            if a>x or b>y or c>z:
                continue
            
            if a==x:
                found[0]=True

            if b==y:
                found[1]=True
            
            if c==z:
                found[2]=True
        return found[0] and found[1] and found[2]