#include <iostream>
#include <vector>
#include "linkedlist/linkedlist.h"

void print(const std::vector<std::string> &toPrint) {
    size_t vec_size = toPrint.size();

    if (vec_size == 0) {
        std::cout << "List is empty" << std::endl;
        return;
    }

    for (size_t i = 0; i < vec_size; i++) {
        std::cout << toPrint.at(i) << " -> ";
    }

    std::cout << "\n";
}


int main() {
    linkedlist::LinkedList ll = linkedlist::LinkedList();
    std::cout << ll.isEmpty() << std::endl;

    ll.append("hello");
    ll.append("world");

    auto found = ll.find("hello");
    std::cout << found << std::endl;

    ll.prepend("before hello!");

    std::cout << "Length: " << ll.length() << std::endl;;
    std::cout << "Slow Length: " << ll.slowLength() << std::endl;
    std::cout << ll.isEmpty() << std::endl;

    auto items = ll.items();
    print(items);

    ll.replace("hello", "hello!");

    items = ll.items();
    print(items);

    ll.remove("before hello!");

    items = ll.items();
    print(items);

    return 0;
}
