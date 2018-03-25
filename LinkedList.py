class Node:

    """ Simple node class, each node contains a value and a pointer to the next Node"""
    def __init__(self, value):
        self.value = value
        self.next = None

    # Getters for value and next
    def getValue(self):
        return self.value

    def getNext(self):
        return self.next

    # To set a pointer to a next node:
    def setNext(self, newNext):
        self.next = newNext

class LinkedList:

    """ Linked list class, made of nodes """
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        """ Takes a value, creates a node with that value
            and attaches it to the list, placing at head
            pointing new node at old head."""

        newNode = Node(value)
        newNode.setNext(self.head)
        self.head = newNode

    def size(self):
        """ Counts nodes as long as they exist, increasing
            count by 1 each time it founds it. Returns count"""

        current = self.head
        count = 0
        while current:
            count += 1
            current = current.getNext() # point to the next node
        return count

    def search(self, value):
        current = self.head
        found = False

        while current and found is False:
            if current.getValue() == value:
                found == True
            else:
                current = current.getNext

        if current is None:
            raise ValueError("Given value not in a list")
        return current

import numpy as np

lst = LinkedList()

print(lst.size())

for i in range(25):
    lst.insert(np.random.randint(0, 301))


while lst.head.getNext is not None:
    print(lst.head.value)
    lst.head = lst.head.getNext()

import numpy as n
