class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max1=0
        ans=0
        for i in range(len(nums)):
            if nums[i]==1:
                max1+=1
            else:
                max1=0
            ans=max(max1,ans)
        return ans