class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_max=nums[0]
        current_min=nums[0]
        answer=nums[0]
        for i in range(1,len(nums)):
            premax=current_max
            premin=current_min
            current_max=max(nums[i],nums[i]*premax,nums[i]*premin)
            current_min=min(nums[i],nums[i]*premax,nums[i]*premin)
            answer=max(answer,current_max)
        return answer