class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        res = []

        product = 1
        zero_count=0

        for num in nums:
            if num==0:
                zero_count+=1
            else:
                product*=num

        for num in nums:
            if zero_count>1:
                res.append(0)
            elif zero_count==1:
                if num==0:
                    res.append(product)
                else:
                    res.append(0)
            else:
                res.append(product//num)

        
        return res