class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count=nums[0]
        for i in range(1,len(nums)):
            count^=nums[i]
        return count