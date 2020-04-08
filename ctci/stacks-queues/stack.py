from linkedlist import LinkedList


class Stack(object):
    def __init__(self):
        self.ll = LinkedList()

    def pop(self):
        return self.ll.pop()

    def push(self, item):
        self.ll.prepend(item)

    def peek(self):
        if self.ll.head == None:
            return None
        return self.ll.head.data

    def isEmpty(self):
        return len(self.ll) == 0

    def items(self):
        return self.ll.items()


if __name__ == "__main__":
    stack = Stack()
    stack.push('hi')
    stack.push('no')
    print(stack.isEmpty())
    print(stack.peek())
