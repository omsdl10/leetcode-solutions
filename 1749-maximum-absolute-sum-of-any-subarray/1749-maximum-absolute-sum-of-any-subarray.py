class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        summ=0
        abssum=0
        for i in range(len(nums)):
            summ+=nums[i]
            abssum=max(abssum,abs(summ))
            if summ<0:
                summ=0
        summ1=0
        abssum1=0
        for i in range(len(nums)):
            summ1+=nums[i]
            abssum1=max(abssum1,abs(summ1))
            if summ1>0:
                summ1=0
        return max(abssum,abssum1)