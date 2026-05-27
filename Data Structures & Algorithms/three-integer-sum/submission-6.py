class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)):
            if i>=1 and nums[i]==nums[i-1]:
                continue
            start=i+1
            end = len(nums)-1
            cur=nums[i]
            while start<end:
                if cur+nums[start]+nums[end]<0:
                    start+=1
                elif cur+nums[start]+nums[end]>0:
                    end-=1
                else:
                    res.append([cur,nums[start],nums[end]])
                    start+=1
                    end-=1
                    while start<end and nums[start]==nums[start-1]:
                        start+=1
                    while start<end and nums[end]==nums[end+1]:
                        end-=1
                    
        return res