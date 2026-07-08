class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ=sum(nums)
        if summ%2==1:
            return False
        summ=summ//2
        dp=[[False for i in range(summ+1)]for j in range(len(nums)+1)]
        for i in range(len(nums)+1):
            dp[i][0]=True
        for i in range(1,len(nums)+1):
            for j in range(1,summ+1):
                if nums[i-1]<=j:
                    dp[i][j]=dp[i-1][j-nums[i-1]] or dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[len(nums)][summ]