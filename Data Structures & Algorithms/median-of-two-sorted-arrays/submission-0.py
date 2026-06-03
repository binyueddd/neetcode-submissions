class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        left=0
        right=min(len(nums1),len(nums2))

        half=(len(nums1)+len(nums2)+1)//2

        while left<=right:
            mid1=(left+right)//2
            mid2=half-mid1

            Aleft=nums1[mid1-1] if mid1>0 else float("-inf")
            Aright=nums1[mid1] if mid1<len(nums1) else float("inf")
            Bleft=nums2[mid2-1] if mid2>0 else float("-inf")
            Bright=nums2[mid2] if mid2<len(nums2) else float("inf")

            if Aleft<=Bright and Bleft<=Aright:
                if (len(nums1)+len(nums2))%2==0:
                    return (max(Aleft,Bleft)+min(Aright,Bright))/2
                else:
                    return max(Aleft,Bleft)
            
            elif Aleft>Bright:
                right=mid1-1
            else:
                left=mid1+1

