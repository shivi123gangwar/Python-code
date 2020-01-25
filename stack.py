class Stack:
    def __init__(self):
        self.stk = []
    def push(self, value):
        self.stk.append(value)
    def pop(self):
        return self.stk.pop(-1)
    def disply(self):
        return self.stk
stkOperations = Stack()
stkOperations.push(10)
stkOperations.push(20)
stkOperations.push(30)
stkOperations.push(40)
print(stkOperations.disply())
print()
stkOperations.pop()
print(stkOperations.disply())

