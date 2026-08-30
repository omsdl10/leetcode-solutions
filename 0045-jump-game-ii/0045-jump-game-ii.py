class Solution:
    def jump(self, nums: List[int]) -> int:
        l=0
        r=0
        jump=0
        for i in range(len(nums)-1):
            r=max(r,i+nums[i])
            if i==l:
                jump+=1
                l=r
        return jump
