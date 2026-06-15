class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operator_mapping = {
            "+":lambda x,y:x+y,
            "-":lambda x,y:x-y,
            "*":lambda x,y:x*y,
            "/":lambda x,y:int(x/y),
        }
        for i in tokens:
            if i not in operator_mapping:
                stack.append(int(i))
            else:
                oper2=stack.pop()
                oper1=stack.pop()
                res=operator_mapping[i](oper1,oper2)
                stack.append(res)
        return stack.pop()
