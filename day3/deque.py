# 双端队列，有队首插入与队尾插入，如果从队首取出，相当于队列，如果从队尾取出，相当于堆栈

class Deque:
    def __init__(self):
        self.items = []

    def addFront(self, item):
        self.items.insert(0, item)
        return item

    def addRear(self, item):
        self.itmes.append(item)
        return item

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    q=Deque()
    q.addFront(1)
    q.addFront(2)
    q.addFront(3)
    q.addFront(4)
    print(q.removeFront())
    print(q.removeFront())
    print(q.removeFront())
    print(q.removeFront())
    print(q.isEmpty())
