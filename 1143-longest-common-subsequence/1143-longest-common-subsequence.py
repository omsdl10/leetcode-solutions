# def lcs(x,y,m,n,dp):
#         if m==0 or n==0:
#             return 0
#         if dp[m][n]!=-1:
#             return dp[m][n]
#         if x[m-1]==y[n-1]:
#             dp[m][n]=1+lcs(x,y,m-1,n-1,dp)
#             return dp[m][n]
#         else:
#             dp[m][n]=max(lcs(x,y,m-1,n,dp),lcs(x,y,m,n-1,dp))
#             return dp[m][n]
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp=[[0]*1001 for i in range(1001)]
        m=len(text1)
        n=len(text2)
        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[m][n]
    