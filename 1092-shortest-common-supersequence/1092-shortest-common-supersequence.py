def lcs(x,y,m,n):
    dp=[[0]*(n+1) for i in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if x[i-1]==y[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    string=""
    i,j=m,n
    while i>0 and j>0:
        if x[i-1]==y[j-1]:
            string+=x[i-1]
            i-=1
            j-=1
        else:
            if dp[i-1][j]>dp[i][j-1]:
                i-=1
            else:
                j-=1
    return string[::-1]
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        string=lcs(str1,str2,len(str1),len(str2))
        i=j=0
        ans=""
        for ch in string:
            while ch!=str1[i]:
                ans+=str1[i]
                i+=1
            while ch!=str2[j]:
                ans+=str2[j]
                j+=1
            ans+=ch
            i+=1
            j+=1
        ans+=str1[i:]
        ans+=str2[j:]
        return ans