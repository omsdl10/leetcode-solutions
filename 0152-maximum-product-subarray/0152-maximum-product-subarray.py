class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxans=nums[0]
        prefix=1
        suffix=1
        for i in range(len(nums)):
            if prefix==0:
                prefix=1
            if suffix==0:
                suffix=1
            prefix=prefix*nums[i]
            suffix=suffix*nums[len(nums)-i-1]
            maxans=max(maxans,max(prefix,suffix))
        return maxans
        
        