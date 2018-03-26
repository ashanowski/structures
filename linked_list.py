#!/usr/bin/env python3.6
from node import Node


class LinkedList:

    """ Linked list class, made of nodes """
    def __init__(self, head=None):
        self.len = 1
        self.comparisons = 0
        self.assigns = 5
        self.head = head
        self.tail = self.head

    def show_counters(self):
        """ Show counters of how many comparisons
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

    def show_list(self):
        """ Prints every element from the linked list """

        current = self.head
        i = 1
        while current.get_value() is not None:
            print('{}:'.format(i), current.get_value())
            i += 1
            if current.get_next() is None:
                break
            else:
                current = current.get_next()

    def append(self, value):
        """ Takes a value, creates a node with that value
            and attaches it to the list, placing at head
            pointing new node at old head."""

        new_node = Node(value, None)
        new_node.set_next(self.head)
        self.head = new_node
        self.len += 1
        self.assigns += 5

    def insert(self, value):


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
        """ Search list for the value
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
