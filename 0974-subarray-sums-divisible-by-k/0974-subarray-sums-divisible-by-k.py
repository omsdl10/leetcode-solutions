class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic={0:1}
        summ=0
        count=0
        for r in range(len(nums)):
            summ+=nums[r]
            mod=summ%k
            if mod<0:
                mod+=k
            if mod in dic:
                count+=dic[mod]
                dic[mod]+=1
            else:
                dic[mod]=1
        return count