class MyQueue:

    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if not self.stack1:
            return 
        while self.stack1:
            ele=self.stack1.pop()
            self.stack2.append(ele)
        rele=self.stack2.pop()
        while self.stack2:
            ele=self.stack2.pop()
            self.stack1.append(ele)
        return rele
    def peek(self) -> int:
        if not self.stack1:
            return 
        while self.stack1:
            ele=self.stack1.pop()
            self.stack2.append(ele)
        rele=self.stack2[-1]
        while self.stack2:
            ele=self.stack2.pop()
            self.stack1.append(ele)
        return rele

    def empty(self) -> bool:
        if not self.stack1:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()