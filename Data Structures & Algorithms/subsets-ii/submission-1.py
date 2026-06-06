class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        path=[]
        nums.sort()
        n=len(nums)
    
        def dfs(i):
            if i==n:
                res.append(path[:])
                return
            
            j=i
            while j<n and nums[j]==nums[i]:
                j+=1
            count=j-i

            dfs(j)

            for c in range(1,count+1):
                path.append(nums[i])
                dfs(j)
            
            for c in range(count):
                path.pop()
            

        dfs(0)
        return res