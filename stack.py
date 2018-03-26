from linked_list import LinkedList
from node import Node

class Stack(LinkedList):
    """ Class imitating stack structure """

    def __init__(self):
        super().__init__()
        self.stack = LinkedList()

    def show(self):
        super().show()

    def push(self, value):
        """ Push the value to the top of stack """
        super().append(value)

    def pop(self):
        """ Pop the value out from the top of stack """
        current = self.head

        if current is None:
            raise ValueError("Stack is empty")
        while current.get_next():
            previous = current
            current = current.get_next()
        previous.set_value(None)
        return previous

    def top(self):
        """ Returns latest stack element """


        # current = self.head
        # if current is None:
            # raise ValueError("Stack is empty")
        # while current.get_next():
            # current = current.get_next()
        # return current
        pass

    def empty(self):
        """ Return true if stack is empty """

        return self.head is None
