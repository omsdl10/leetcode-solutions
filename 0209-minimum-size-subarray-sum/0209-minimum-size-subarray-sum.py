class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        min_len=float('inf')
        summ=0
        for r in range(len(nums)):
            summ+=nums[r]
            while summ>=target:
                min_len=min(min_len,r-l+1)
                summ-=nums[l]
                l+=1
        if min_len==float('inf'):
            return 0
        return min_len