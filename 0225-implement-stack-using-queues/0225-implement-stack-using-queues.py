class MyStack:

    def __init__(self):
        self.st = deque()

    def push(self, x: int) -> None:
        self.st.append(x)
        self.st.rotate(1)
        
    def pop(self) -> int:
        ele = self.st[0]
        self.st.popleft()
        return ele
        
    def top(self) -> int:
        return self.st[0]
        
    def empty(self) -> bool:
        return len(self.st) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()