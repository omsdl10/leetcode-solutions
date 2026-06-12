class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i=='[' or i=='{' or i=='(':
                stack.append(i)
            else:
                if stack:
                    top=stack.pop()
                    if top=='[' and i==']':
                        continue
                    if top=='(' and i==')':
                        continue
                    if top=='{' and i=='}':
                        continue
                return False
        return len(stack)==0
                