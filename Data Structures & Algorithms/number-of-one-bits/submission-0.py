class Solution:
    def hammingWeight(self, n: int) -> int:
        quotient = 0
        digit=0
        ans=0
        # less_zero=False
        # if n<0:
        #     less_zero=True
        #     n=abs(n)

        while n!=0:
            digit=n%2
            n//=2
            ans+=digit
        return ans 
