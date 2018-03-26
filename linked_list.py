#!/usr/bin/env python3.6
from node import Node
import numpy as np


class LinkedList:
    """ Linked list class, made of nodes """

    def __init__(self, head=None):
        self.len = 1
        self.comparisons = 0
        self.assigns = 5
        self.head = head
        self.tail = self.head

    def show_counters(self):
        """
        Show counters of how many comparisons
        and assigns were made

        """
        print('Comparisons made: ', self.comparisons)
        print('Assigns made: ', self.assigns)
        print('Operations in total: ', self.comparisons
                                     + self.assigns)

    def reset_counters(self):
        """ Resets counters """
        self.comparisons = 0
        self.assigns = 0

    def show(self):
        """ Prints every element from the linked list """

        current = self.head
        if current is None:
            raise ValueError("List is empty")
        i = 1
        while current.get_value() is not None:
            print('{}:'.format(i), current.get_value())
            i += 1
            if current.get_next() is None:
                break
            else:
                current = current.get_next()

    def append(self, value):
        """
        Takes a value, creates a node with that value
        and attaches it to the tail of the list

        """

        if self.head == None:
            self.head = Node(value)
        else:
            current = self.head
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(Node(value))

    def insert(self, value):
        """
        Inserts a value at the beginning of the list,
        attaching it to the head

        """

        new_node = Node(value)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        """
        Counts nodes as long as they exist, increasing
        count by 1 each time it founds it. Returns Counts

        """

        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next() # point to the next node
        return count

    def search(self, value):
        """
        Search list for the value
        and return the node containing it

        """

        current = self.head
        found = False
        while current and found is False:
            if current.get_value() == value:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Given value not in a list")
        return current

    def delete(self, value):
        """ Delete element based on value """

        current = self.head
        found = False
        previous = None
        while current and found is False:
            if current.get_value() == value:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Value not found")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())


def fill_by_appending(structure):
    """
    Fills the structure with 25 random integers
    from [0, 300] range

    """

    for _ in range(25):
        structure.append(np.random.randint(0, 301))
    return structure

def fill_mixed(structure):
    """
    Fills the list once with append, then with insert """
    i = 0
    while i < 25:
        structure.append(np.random.randint(0, 301))
        i += 1
        if i == 25:
            break
        else:
            structure.insert(np.random.randint(0, 301))
            i += 1

def fill_random(structure):
    """ Fills the list randomly, either at start, or beggining """
    i = 0
    while i < 25:
        rand = np.random.random_sample(1)
        if rand < 0.5:
            structure.append(np.random.randint(0, 301))
            i += 1
        else:
            structure.insert(np.random.randint(0, 301))
            i += 1
    return structure
