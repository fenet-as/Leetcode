class MinStack:
    '''
    '''

    def __init__(self):
        self.st = []
        self.min = float('inf')

    
        

    def push(self, val: int) -> None:
        if val < self.min:
            self.min = val
        
        self.st.append((val,self.min))
        

    def pop(self) -> None:
        self.st.pop()
        if self.st:
            le = self.st[-1]
            self.min = le[1]
        else:
            self.min = float('inf')

        

    def top(self) -> int:
        le = self.st[-1]
        return le[0]
        

    def getMin(self) -> int:
        le = self.st[-1]
        return le[1]
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()