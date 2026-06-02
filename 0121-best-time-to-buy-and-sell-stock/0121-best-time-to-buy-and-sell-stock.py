class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        array=[]
        maxnumber=prices[-1]
        for i in range(len(prices)-1,-1,-1):
            num=max(maxnumber,prices[i])
            array.append(num)
            maxnumber=num
        array.reverse()
        for i in range(len(prices)):
            prices[i]=array[i]-prices[i]
        return max(prices)


