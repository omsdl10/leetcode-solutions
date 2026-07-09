def lcs(x,y,m,n,dp):
        if m==0 or n==0:
            return 0
        if dp[m][n]!=-1:
            return dp[m][n]
        if x[m-1]==y[n-1]:
            dp[m][n]=1+lcs(x,y,m-1,n-1,dp)
            return dp[m][n]
        else:
            dp[m][n]=max(lcs(x,y,m-1,n,dp),lcs(x,y,m,n-1,dp))
            return dp[m][n]
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp=[[-1]*1001 for i in range(1001)]
        m=len(text1)
        n=len(text2)
        return lcs(text1,text2,m,n,dp)
    