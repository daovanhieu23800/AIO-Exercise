class MyQueue():
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

    def dequeue(self):
        if self.is_empty():
            return "There is no element to pop"
        else:
            item = self.__stack.pop(0)
            return item

    def enqueue(self, value):
        if self.is_full():
            return "Can't push more item to the queue"
        else:
            item = self.__stack.append(value)
            return item

    def front(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            item = self.__stack[0]
            return item


queue1 = MyQueue(max_cap=5)
queue1.enqueue(1)
queue1.enqueue(2)
print(queue1.is_full())
print(queue1.front())
print(queue1.dequeue())
print(queue1.front())
print(queue1.dequeue())
print(queue1.is_empty())
