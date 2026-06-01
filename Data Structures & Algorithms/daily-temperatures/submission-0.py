class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        res=[0]*len(temperatures)

        for i, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<temperature:
                pre=stack.pop()
                res[pre]=i-pre
            
            stack.append(i)
        
        return res
