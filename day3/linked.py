
# 节点
class Node():
    def __init__(self, item):
        self.item = item
        self.next = None

# 链表


class linked():
    def __init__(self):
        self._head = None

    # 从头插入
    def add(self, item):
        if item is None:
            return None
        node = Node(item)
        node.next = self._head
        self._head = node

    # 从尾部插入
    def append(self, item):
        node = Node(item)
        if self._head is None:
            self._head = node
            return
        cur = self._head
        pre = None
        while cur:
            pre = cur
            cur = cur.next
        pre.next = node

    def size(self):
        cur = self._head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def isEmpty(self):
        return self._head is None

    def travel(self):
        cur = self._head
        while cur:
            print(cur.item.item)
            cur = cur.next

    # 翻转链表1->2-3  变成3->2-1

    def reverse(self):
        cur = self._head
        pre = None
        next_node = cur.next
        while cur:
            cur.next = pre
            pre = cur
            cur = next_node
            if cur:
                next_node = cur.next
        self._head = pre


if __name__ == "__main__":
    link = linked()
    link.append(Node(1))
    link.append(Node(2))
    link.append(Node(3))
    link.append(Node(4))
    link.reverse()
    link.travel()
