class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        new=""
        count=0
        for i in s:   
            if count==0 and i=='(':
                count+=1
                continue
            if count==1 and i==')':
                count=0
                continue
            if i=='(':
                count+=1
            else:
                count-=1
            new+=i
        return new


