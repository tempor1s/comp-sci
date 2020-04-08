class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, items=None):
        self.head = None
        if items:
            for item in items:
                self.append(item)

    def append(self, item):
        node = Node(item)
        if self.head is None:
            self.head = node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = node

    def prepend(self, item):
        node = Node(item)
        node.next = self.head
        self.head = node

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
                node.next = node.next.next
            node = node.next


if __name__ == "__main__":
    ll = LinkedList([10, 10, 5, 3, 2, 1, 7, 7, 12, 13, 13])
    print(ll.items())
    print(ll.items())
