

class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        return item

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0

    def peek(self):
        return self.items[-1]


class Queue():
    def __init__(self):
        self.items = []

    def enque(self, item):
        self.items.insert(0, item)
        return item

    def deque(self):
        return self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def playGame():
    list = ['A', 'B', 'C', 'D', 'E', 'F']
    queue = Queue()
    for i in range(6):
        queue.enque(list[i])
    while queue.size() > 1:
        for i in range(20):
            queue.enque(queue.deque())
        queue.deque()
    return queue.deque()


if __name__ == '__main__':

    # queue = Queue()
    # list = [1, 2, 3, 4]
    # for i in list:
    #     print(queue.enque(i))
    # print(queue.peek())
    # print(queue.deque())
    # print(queue.deque())
    # print(queue.deque())
    # print(queue.deque())
    # print(queue.isEmpty())
    print(playGame())

# 击鼓传花游戏，第一秒开始传递，敲七次传6下的那个人淘汰。找出获胜的那个序号,使用队列Queue
