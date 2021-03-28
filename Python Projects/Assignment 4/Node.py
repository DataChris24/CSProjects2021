"""
Title: Node Class
Author: Christopher Mims
Date: 14 October 2020
Description: This class will create nodes to be used in a linked list
"""

class Node:

    # This initializes the Node object
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.data)

    # This will return the data of the node
    def get_data(self):
        return self.data

    # This will return the pointer to the next node
    def get_next(self):
        return self.next

    # This will return the pointer to the previous node
    def get_prev(self):
        return self.prev

    # This will set/change the data of a node
    def set_data(self, newData):
        self.data = newData

    # This will set/change the next pointer of the node
    def set_next(self, newNext):
        self.next = newNext

    # This will set/change the prev pointer of the node
    def set_prev(self, newPrev):
        self.prev = newPrev

