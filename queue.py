from linked_list import LinkedList

class Queue(LinkedList):
    """ Imitates queue data structure """

    def __init__(self):
        super().__init__()

    def enqueue(self, value):
        """ Add an element to the queue """

        super().append(value)

    def dequeue(self):
        """ Remove the last element of the queue """

        value = self.head.get_value()
        super().delete(value)
        return value
