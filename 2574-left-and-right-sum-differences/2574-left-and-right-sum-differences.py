class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return [0]
        answer=[]
        left=[0]
        right=[0]
        summ=0
        for i in range(len(nums)-1):
            summ+=nums[i]
            left.append(summ)
        summ=0
        for i in range(len(nums)-1,0,-1):
            summ+=nums[i]
            right.append(summ)
        right=right[::-1]
        for i in range(len(nums)):
            ans=abs(left[i]-right[i])
            answer.append(ans)
        return answer