class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dic={0:-1}
        summ=0
        for i in range(len(nums)):
            summ+=nums[i]
            remainder=summ%k
            if remainder in dic:
                if i-dic[remainder]>=2:
                    return True 
            else:
                dic[remainder]=i
        return False

        