class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        num=0
        string=""
        for i in s:
            if i.isdigit():
                num=num*10+int(i)
            elif i=='[':
                stack.append((string,num))
                num=0
                string=""
            elif i==']':
                prev,repeat=stack.pop()
                string=prev+repeat*string
            else:
                string+=i
        return string

