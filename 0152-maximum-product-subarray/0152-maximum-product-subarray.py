class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans=nums[0]
        max_num=nums[0]
        min_num=nums[0]
        for i in range(1,len(nums)):
            maxnum=max(nums[i],nums[i]*max_num,nums[i]*min_num)
            minnum=min(nums[i],nums[i]*max_num,nums[i]*min_num)
            max_num=maxnum
            min_num=minnum
            ans=max(ans,max_num)
        return ans
        
        