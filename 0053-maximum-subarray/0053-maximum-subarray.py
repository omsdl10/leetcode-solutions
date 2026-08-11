class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        summ=0
        ans=nums[0]
        for i in range(len(nums)):
            if summ<0:
                summ=0
            summ+=nums[i]
            ans=max(summ,ans)
        return ans