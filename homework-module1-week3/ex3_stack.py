class MyStack():
    def __init__(self, max_cap: int) -> None:
        self.max_cap = max_cap
        self.__stack = []

    def is_empty(self):
        if len(self.__stack) == 0:
            return True
        else:
            return False

    def is_full(self):
        if len(self.__stack) == self.max_cap:
            return True
        else:
            return False

    def pop(self):
        if self.is_empty():
            return "There is no element to pop"
        else:
            item = self.__stack.pop()
            return item

    def push(self, value):
        if self.is_full():
            return "Can't push more item to the stack"
        else:
            item = self.__stack.append(value)
            return item

    def top(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            item = self.__stack[-1]
            return item


stack1 = MyStack(max_cap=5)
stack1.push(1)
stack1.push(2)
print(stack1.is_full())
print(stack1.top())
print(stack1.pop())
print(stack1.top())
print(stack1.pop())
print(stack1.is_empty())
