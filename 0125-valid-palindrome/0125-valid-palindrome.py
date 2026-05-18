class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=[]
        for i in range(len(s)):
            if s[i].isalnum():
                res.append(s[i].lower())
        if res==[]:
            return True
        left=0
        right=len(res)-1
        while left<=right:
            if res[left]!=res[right]:
                return False
            left+=1
            right-=1
        return True
            
