from linked_list import LinkedList


class LL(LinkedList):
    def __init__(self, items):
        super().__init__(items)

    def remove_duplicates(self):
        seen = []
        node = self.head

        seen.append(node.data)
        while node.next is not None:
            if node.next.data in seen:
                node.next = node.next.next
            else:
                seen.append(node.next.data)
                node = node.next


if __name__ == "__main__":
    ll = LL([10, 10, 5, 3, 2, 1, 7, 7, 12, 13, 13])
    print(ll.items())
    ll.remove_duplicates()
    print(ll.items())
