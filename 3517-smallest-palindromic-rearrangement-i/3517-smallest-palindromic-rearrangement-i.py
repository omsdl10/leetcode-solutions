class Solution:
    def smallestPalindrome(self, s: str) -> str:
        if len(s)==1:
            return s
        n=len(s)
        ls=[]
        for i in range(n//2):
            ls.append(s[i])
        ls.sort()
        new ="".join(ls)
        if n%2==1:
            mid=s[n//2]
            reverse=new[::-1]
            new=new+mid+reverse
        else:
            reverse=new[::-1]
            new=new+reverse
        return new