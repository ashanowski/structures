from linked_list import Node, LinkedList
import numpy as np

lst = LinkedList()

for _ in range(24):
    lst.insert(np.random.randint(0, 300))
