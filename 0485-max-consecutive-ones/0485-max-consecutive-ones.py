class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result=0
        res=0
        for i in range(len(nums)):
            if nums[i]==1:
                result+=1
            else:
                result=0
            res=max(res,result)
        return res


