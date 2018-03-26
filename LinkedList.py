import numpy as np

class Node:

    """ Simple node class, each node contains a value and a pointer to the next Node"""
    def __init__(self, value):
        self.value = value
        self.next = None

    # Getters for value and next
    def get_value(self):
        """ Return current value """
        return self.value

    def get_next(self):
        """ Return next node """
        return self.next

    # To set a pointer to a next node:
    def set_next(self, new_next):
        """ Set _next pointer to the next node """
        self.next = new_next

class LinkedList:

    """ Linked list class, made of nodes """
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        """ Takes a value, creates a node with that value
            and attaches it to the list, placing at head
            pointing new node at old head."""

        new_node = Node(value)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        """ Counts nodes as long as they exist, increasing
            count by 1 each time it founds it. Returns count"""

        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next() # point to the next node
        return count

    def search(self, value):
        """ Search list for the value and return it """
        current = self.head
        found = False

        while current and found is False:
            if current.get_value() == value:
                found = True
            else:
                current = current.get_next

        if current is None:
            raise ValueError("Given value not in a list")
        return current

    def delete(self, value):
        """ Delete element based on value """

        current = self.head
        found = False
        previous = None
        while current and found is False:
            if current.get_value == value:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Value not found")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next)


LST = LinkedList()

print(LST.size())

for _ in range(25):
    LST.insert(np.random.randint(0, 301))


while LST.head.get_next is not None:
    print(LST.head.value)
    LST.head = LST.head.get_next()
