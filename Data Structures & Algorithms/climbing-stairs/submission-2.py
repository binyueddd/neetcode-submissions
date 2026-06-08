class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        dp0=1
        dp1=2
        for i in range(2,n):
            dp0,dp1=dp1,dp0+dp1
        return dp1