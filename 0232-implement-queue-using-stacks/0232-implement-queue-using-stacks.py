class MyQueue:

    def __init__(self):
        # We will have two stacks, one for loading and another for unloading
        self.stck1 = []
        self.stck2 = []
    def reverse(self):
        # when we call this function, we will basically just reverse the sequence
        
        while self.stck1:
            self.stck2.append(self.stck1.pop())       

    def push(self, x: int) -> None:
        # pushing elements in stack 1
        self.stck1.append(x)
        

    def pop(self) -> int:
        # only reversing the stack, when the stack 2 is empty and return the top element 
        while not self.stck2:
            self.reverse()
        return self.stck2.pop()
        

    def peek(self) -> int:
        # again reverse the array if stack2 is empty
        
        while not self.stck2:
            self.reverse()
        return self.stck2[-1]
        

    def empty(self) -> bool:
        # check if there is any elements 
        return self.stck2 == [] and self.stck1 == []
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()