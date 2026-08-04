class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        new=[]
        nums.sort()
        for i in range(nums[0],nums[-1]):
            if i not in nums:
                new.append(i)
        return new
