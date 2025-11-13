'''
[1,2,3,4,5]
[5,2,3,4,1]
'''
class MyQueue:

    def __init__(self):
        self.st = []

        

    def push(self, x: int) -> None:
        self.st.append(x)

    def pop(self) -> int:
        self.st.reverse()
        e = self.st.pop()
        self.st.reverse()
        return e
        

    def peek(self) -> int:
        return self.st[0]
        

    def empty(self) -> bool:
        if len(self.st) > 0:
            return False
        return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()