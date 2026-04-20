class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dic={0:-1}
        summ=0
        for i in range(len(nums)):
            summ+=nums[i]
            if summ%k not in dic:
                dic[summ%k]=i
            elif i-dic[summ%k]>=2:
                    return True
        return False

        