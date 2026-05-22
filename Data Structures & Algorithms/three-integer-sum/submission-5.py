class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)):
            if i>=1 and nums[i]==nums[i-1]:
                continue
            start = i+1
            end = len(nums)-1
            while start<end:

                if nums[i]+nums[start]+nums[end]>0:
                    end-=1
                elif nums[i]+nums[start]+nums[end]<0:
                    start+=1
                else:
                    res.append([nums[i],nums[start],nums[end]])
                    start+=1
                    end-=1
                    while start<end and nums[start]==nums[start-1]:
                        start+=1
                    while start<end and nums[end]==nums[end+1]:
                        end-=1
                
        return res