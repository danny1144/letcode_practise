class Node():
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None


class Tree():
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur = queue.pop(0)
            if not cur.left:
                cur.left = node
                return
            if not cur.right:
                cur.right = node
                return

            queue.append(cur.left)
            queue.append(cur.right)

    # 广度优先遍历，层次遍历
    def travel(self):
        if self.root is None:
            return None
        q = [self.root]
        res = [self.root.item]
        while q:
            cur = q.pop(0)
            if cur.left is not None:
                q.append(cur.left)
                res.append(cur.left.item)
            if cur.right is not None:
                q.append(cur.right)
                res.append(cur.right.item)
        return res

    # 前序遍历
    def preOrder(self, root):
        if root is None:
            return []
        result = [root.item]
        left = self.preOrder(root.left)
        right = self.preOrder(root.right)
        return result + left + right
    # 中序遍历

    def middleOrder(self, root):
        if root is None:
            return []
        result = [root.item]
        left = self.preOrder(root.left)
        right = self.preOrder(root.right)
        return left + result + right

    # 后序遍历

    def afterOrder(self, root):
        if root is None:
            return []
        result = [root.item]
        left = self.preOrder(root.left)
        right = self.preOrder(root.right)
        return left + right + result


if __name__ == "__main__":
    tree = Tree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)

    print(tree.afterOrder(tree.root))
