from linkedlist import LinkedList


class Queue(LinkedList):
    def __init__(self):
        self.ll = LinkedList()

    def add(self, item):
        self.ll.append(item)

    def remove(self):
        # remove first item in the list
        self.ll.pop()

    def peek(self):
        # return top of the queue
        if self.ll.head == None:
            return None
        return self.ll.head.data

    def isEmpty(self):
        # return true if queue is empty
        return len(self.ll) == 0

    def items(self):
        return '->'.join(self.ll.items())


if __name__ == "__main__":
    q = Queue()
    q.add('hi')
    q.add('lol')
    print(q.peek())
    print(q.items())
    q.remove()
    print(q.items())
