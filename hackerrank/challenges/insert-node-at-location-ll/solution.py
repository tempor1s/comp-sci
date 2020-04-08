#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the insertNodeAtPosition function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtPosition(head, data, position):
    new_node = SinglyLinkedListNode(data)

    if position == 0:
        # the head node
        new_node.next = head
        return new_node

    node = head
    # to hold current position in the list
    temp = 1
    # starts at the node after the head
    while node.next is not None:
        if position == 1:
            new_node.next = node
            head.next = new_node

        if position == temp:
            new_node.next = node.next
            node.next = new_node
            return head

        node = node.next
        # now the second item after the head (head, item, (item2)) and so on
        temp += 1

if __name__ == '__main__':
