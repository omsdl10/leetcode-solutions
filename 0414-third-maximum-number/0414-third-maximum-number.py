class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        ls=[]
        for i in range(len(nums)):
            if nums[i] in ls:
                continue
            ls.append(nums[i])
        ls.sort()
        if len(ls)<=2:
            return ls[-1]
        else:
            return ls[-3]