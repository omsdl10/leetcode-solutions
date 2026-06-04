class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        sumo=0
        for i in nums:
            sumo|=i
        return sumo*(1<<(len(nums)-1))