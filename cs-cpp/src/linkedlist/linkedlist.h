#pragma once

#include <vector>
#include <iostream>
#include <string>

namespace linkedlist {
struct Node {
    std::string data;
    Node *next;
};

class LinkedList {
 private:
    Node *head, *tail;
    int size;
 public:
    LinkedList();
    void append(const std::string data);
    void prepend(const std::string data);
    void remove(const std::string &data);
    std::vector<std::string> items();
    bool isEmpty();
    int length();
    int slowLength();
    std::string find(const std::string &data);
    void replace(const std::string &toReplace, const std::string replaceWith);
};

}  // namespace linkedlist
