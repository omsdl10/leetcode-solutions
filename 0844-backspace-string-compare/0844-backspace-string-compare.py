def build(s):
    stack=[]
    for i in s:
        if i=='#':
            if stack:
                stack.pop()
        else:
            stack.append(i)
    return stack
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return build(s)==build(t)
