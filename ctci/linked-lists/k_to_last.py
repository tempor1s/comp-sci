from linked_list import LinkedList


class LL(LinkedList):
    def __init__(self, items):
        super().__init__(items)

    def k_to_last(self, k):
        length = 0
        node = self.head
        while node is not None:
            length += 1
            node = node.next

        k_to_last_num = length - k + 1
        node = self.head
        nodes = []
        temp = 0
        while node is not None:
            temp += 1
            if temp >= k_to_last_num:
                nodes.append(node.data)
            node = node.next
        return nodes


if __name__ == "__main__":
    ll = LL([10, 10, 5, 3, 2, 1, 7, 7, 12, 13, 13])
    print(ll.items())
    print(ll.k_to_last(3))
