#include "linkedlist.h"

#include <vector>
#include <iostream>

namespace linkedlist {
    // String Implementation
    LinkedList::LinkedList() {
        this->head = NULL;
        this->tail = NULL;
        this->size = 0;
    }

    void LinkedList::append(const std::string data) {
        Node *tmp = new Node;
        tmp->data = data;
        tmp->next = NULL;

        if (head == NULL) {
            head = tmp;
            tail = tmp;
        } else {
            tail -> next = tmp;
            tail = tail->next;
        }

        size++;
    }

    void LinkedList::prepend(const std::string data) {
        Node *tmp = new Node;
        tmp->data = data;

        if (head == NULL) {
            tmp->next = NULL;
            head = tmp;
            tail = tmp;
        } else {
            tmp->next = head;
            head = tmp;
        }

        size++;
    }

    void LinkedList::remove(const std::string &toDelete) {
        Node *node = head;
        Node *prev = NULL;

        while (node != NULL) {
            if (node->data == toDelete) {
                if (prev == NULL) {
                    head = node->next;
                    if (node->next == NULL) {
                        tail = NULL;
                    }
                } else if (node->next == NULL) {
                    prev->next = NULL;
                    tail = prev;
                } else {
                    prev->next = head->next;
                }

                size--;
                free(prev);

                return;
            } else {
                prev = node;
                node = node->next;
            }
        }

        free(prev);

        std::cout << "Could not find item to delete." << std::endl;
    }

    std::vector<std::string> LinkedList::items() {
        std::vector<std::string> words;

        Node *node = head;

        while (node != NULL) {
            words.push_back(node->data);
            node = node->next;
        }

        return words;
    }

    bool LinkedList::isEmpty() {
        return head == NULL ? true : false;
    }

    // Just return the size - potentially incorrect
    int LinkedList::length() {
        return size;
    }

    // Loop through and count the size - o(n) but always correct
    int LinkedList::slowLength() {
        int count = 0;

        Node *node = head;
        while (node != NULL) {
            count++;
            node = node->next;
        }

        return count;
    }

    std::string LinkedList::find(const std::string &toFind) {
        if (head == NULL) {
            return "";
        }

        if (toFind == tail->data) {
            return tail->data;
        }

        Node *node = head;
        while (node != NULL) {
            if (toFind == node->data) {
                return node->data;
            } else {
                node = node->next;
            }
        }

        return "";
    }

    void LinkedList::replace(
            const std::string &replace,
            const std::string replacement) {
        Node *node = head;

        while (node != NULL) {
            if (node->data == replace) {
                node->data = replacement;
                return;
            } else {
                node = node->next;
            }
        }
    }

    // Mby add int implementation?
}  // namespace linkedlist
