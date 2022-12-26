
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

class MyQueue:
    def __init__(self):
        self.items = []
    
    def push(self, x: int) -> None:
        self.items.append(x)

    def pop(self) -> int:
        pop = self.items[0]
        self.items.remove(pop)
        return pop

    def peek(self) -> int:
        return self.items[0]

    def empty(self) -> bool:
        return True if len(self.items) == 0 else False
    
    def display(self) -> list:
        lst = []
        
        if len(self.items) == 0:
            return
        for i in self.items:
            lst.append(i)
        return lst