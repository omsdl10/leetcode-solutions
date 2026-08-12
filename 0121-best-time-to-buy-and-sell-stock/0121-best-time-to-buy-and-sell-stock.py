class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minnumber=prices[0]
        maxdiff=0
        for i in range(len(prices)):
            if prices[i]<minnumber:
                minnumber=prices[i]
            diff=prices[i]-minnumber
            maxdiff=max(diff,maxdiff)
            
        return maxdiff