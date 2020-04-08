class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, items=None):
        self.head = None
        self.length = 0
        if items:
            for item in items:
                self.append(item)

    def __len__(self):
        return self.length

    def append(self, item):
        node = Node(item)
        if self.head is None:
            self.head = node
            self.length += 1
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = node
        self.length += 1

    def prepend(self, item):
        node = Node(item)
        node.next = self.head
        self.head = node
        self.length += 1

    def items(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        return nodes

    def delete(self, item):
        node = self.head
        if node.data == item:
            self.head = node.next

        while node.next is not None:
            if node.next.data == item:
                self.length -= 1
                node.next = node.next.next
            node = node.next

    def pop(self):
        head = self.head
        node = self.head.next
        self.head = node
        return head.data
