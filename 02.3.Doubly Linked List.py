"""

"""


class DoubleLinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None #
            self.prev = None # link to previously Node

    def __init__(self):
        self.head = None # first elem
        self.tail = None # last elem
        self.size = 0 # count elements

    # insert elem in tail in list
    def append(self, value):
        pass
    # insert elem in head of list
    def prepend(self, value):
        pass
    # insert elem to index
    def insert(self, elem):
        pass
    # delete first find elem
    def remove(self,value):
        pass
    # return and delete last elem
    def pop(self):
        pass
    # return and delete first elem
    def pop_first(self):
        pass
    # return True if elem in list
    def find(self,value):
        pass
    # return elements of list
    def display(self):
        pass
    # return reverse elements of list
    def reverse(self):
        pass


