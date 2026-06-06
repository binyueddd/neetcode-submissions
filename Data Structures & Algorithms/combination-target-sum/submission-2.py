class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        res=[]
        path=[]
        sum=0
        nums.sort()

        def dfs(i,sum):
            if sum==target:
                res.append(path[:])
                return

            if i==n or sum+nums[i]>target:
                return

            dfs(i+1,sum)
            
            if sum+nums[i]<=target:
                path.append(nums[i])
                dfs(i,sum+nums[i])
                path.pop()
        
        dfs(0,0)
        return res


            