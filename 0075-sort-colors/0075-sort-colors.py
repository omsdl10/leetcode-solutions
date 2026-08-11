class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        u=0
        j=len(nums)-1
        while u<=j:
            if nums[u]==0:
                nums[i],nums[u]=nums[u],nums[i]
                i+=1
                u+=1
            elif nums[u]==2:
                nums[u],nums[j]=nums[j],nums[u]
                j-=1
            else:
                u+=1
        