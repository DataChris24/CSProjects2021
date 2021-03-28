"""
Title: Linked List Class
Author: Christopher Mims
Date: 14 October 2020
Description: This class will create a singularly linked list
"""
import numpy as np
import time 
import Node
import math

mergeopers = 0


class LinkedList:

    def __init__(self):
        '''
        This creates an empty list. Needs no parameters and returns an empty list.
        '''
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        '''
        This will print out the list with an arrow pointing showing which node
        points to which node
        '''
        list_str = ""
        curr = self.head
        while curr is not None:
            list_str += str(curr)
            list_str += "->"
            curr = curr.get_next()
        list_str += "None"
        return list_str

    def add(self, item):
        '''
        This will add a node to the end of the list
        '''
        temp = Node.Node(item)
        temp.set_next(self.head)
        self.head = temp
        self.size += 1

    def append(self, item):
        '''
        Adds a new item to the end of the list, making it the last item in 
        the collection. It needs the item and returns nothing. Assumes that
        the itme is not already in the list.
        '''
        if self.head == None:
            self.add(item)
        else:
            curr = self.head
            while curr.get_next() is not None:
                curr = curr.get_next()
            temp = Node.Node(item)
            curr.set_next(temp)
            self.size += 1
        return self.size - 1

    def insert(self, index, item):
        '''
        Adds a new item to the list at the specified position pos. It needs the
        item and returns nothing. Assumes the item is not already in the list
        and there are enough existing items to have position pos.
        '''
        if index == 0:
            self.add(item)
        else:
            curr = self.head
            i = 0
            while curr.get_next() is not None and i < index - 1:
                curr = curr.get_next()
                i += 1
            temp = Node.Node(item)
            temp.set_next(curr.get_next())
            curr.set_next(temp)

    def pop(self, index=None):
        '''
        Removes and returns the item at position index. It needs the position 
        and returns the item.
        If index is not specified, removes and returns the last item in the 
        list.
        Assumes the item is in the list.
        '''
        if index is None:
            index = self.size() - 1

        if index == 0:
            curr = self.head
            self.head = self.head.get_next
            self.size -= 1
            return curr
        else:
            curr = self.head 
            i = 0 
            while curr.get_next() is not None and i < index - 1:
                curr = curr.get_next()
                i += 1
            to_pop = curr.get_next()
            curr.set_next(to_pop.get_next())
            self.size -= 1
            return to_pop

    def replace_data(self, index, data):
        if index == 0:
            curr = self.head
            curr.set_data(data)
        else:
            curr = self.head 
            i = 0
            while curr.get_next() is not None and i != index:
                curr = curr.get_next()
                i += 1
            curr.set_data(data)


    def data_index(self, index):
        '''
        Finds an item at the specified index. Returns that item's data.
        Assumes index is in the list.
        '''
        count = 0
        curr = self.head
        while count != index:
            curr = curr.get_next()
            count += 1
        return curr.get_data()

    def remove(self, item):
        '''
        Removes the item from the list. It needs the item and modifies the list.
        Assumes the item is present in the list.
        '''
        current = self.head
        previous = None 
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current 
                current = current.get_next()

        if previous == None:
            self.head = current.get_next()
            self.size -= 1
        else:
            previous.set_next(current.get_next()) 
            self.size -= 1
        return self.size 

    def search(self, item):
        '''
        Searches for the item in the list. It needs the item and returns the 
        index of the item (None if not found).
        Combined a Boolean search(item) with index(item) function.
        '''
        current = self.head 
        found = None
        loc = 0
        while current != None and found == None:
            if current.get_data() == item:
                found = loc
            else:
                current = current.get_next()
                loc += 1

        return found

    def is_empty(self):
        '''
        Tests to see wheter the list is empty. It needs no parameters and 
        returns a boolean value.
        '''
        return self.head == None

    def size(self):
        '''
        Returns the number of items in the list. It needs no parameters and 
        returns an integer.
        '''
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next() 
        return count 

    def from_array(self, array):
        '''
        This will create a linked list from an array by adding each item in the
        array to the list with the add() function.
        It takes a list and an array of items. Returns the linked list.
        '''
        for i in range(len(array)):
            self.add(array[i])

    def selection_sort(self):
        '''
        This will perform Selection Sort on the linked list. Does not take any 
        inputs and returns the number of operations operations and elapsed
        time elpstime.
        '''
        start = time.time()
        operations = 1
        curr = self.head
        while curr:
            min = curr
            next = curr.get_next()
            operations += 3
            while next:
                operations += 1
                if min.get_data() > next.get_data():
                    min = next
                    operations += 1
                next = next.get_next()
                operations += 2
            temp = curr.get_data()
            curr.data = min.data 
            min.data = temp 
            curr = curr.get_next()
            operations += 4
        end = time.time()
        elpstime = end - start
        return operations, elpstime
    
    def bubble_sort(self):
        '''
        This will perform Bubble Sort on the linked list. Does not take any 
        inputs and returns the number of operations operations and elapsed
        time elpstime.
        '''
        start = time.time()
        swap = 0
        operations = 0
        curr = self.head 
        while curr:
            min = curr 
            next = curr.get_next()
            operations += 2
            while next:
                if min.get_data() > next.get_data():
                    swap += 1
                    temp = next.get_data()
                    next.data = min.data
                    min.data = temp 
                    operations += 4
                next = next.get_next()
                operations += 3
            if swap == 0:
                operations += 1
                break 
            curr = curr.get_next()
            operations += 1
        operations += 3    
        end = time.time()
        elpstime = end - start
        return operations, elpstime
    
    def merge_sort(self, head):
        '''
        This will perform the Merge Sort on the linked list. Recursively
        separates the list into smaller lists by sending the head node
        to itself, finds the middle of the list, sets middle element's 
        next point to None (making it into two lists) and then sending
        each head node back into recursive call. Returns the sorted list.
        Help with this method was found at: https://www.geeksforgeeks.org/merge-sort-for-linked-list/
        '''
        if head == None or head.get_next() == None:  # Base case if head is None or has next pointer equal to None
            return head

        # The following steps separate the list into two sublists by finding the middle and setting the middle's
        # next pointer to None
        middle = self.get_middle(head)  # Gets the middle element of the list
        next_to_middle = middle.get_next()  
        middle.next = None  # Sets the next pointer of the middle element to None

        left = self.merge_sort(head)  # Recursively separate the left list
        right = self.merge_sort(next_to_middle)  # Recursively separate the right list

        return self.merge_lists(left, right)  # Merges the two list, sorting as it goes
    
    def merge_lists(self, left, right):
        '''
        Helper function of merge_sort to merge the left and right lists.
        Takes a left and right list. Returns the sorted list.
        '''
        result = None
        if left == None:  # If left list is empty returns the right list
            return right 
        if right == None:   # If right list is empty returns the left list
            return left 
        if left.data < right.data:
            result = left 
            result.next = self.merge_lists(left.get_next(), right)
        else:
            result = right
            result.next = self.merge_lists(left, right.get_next())
        return result 

    def get_middle(self, head):
        '''
        Helper function of merge_sort to find the middle of the linked list. 
        Takes the head Node and iterates through to find middle. Returns the 
        middle element of the linked list.
        '''
        if head == None:
            return head
        slow = head
        fast = head 
        while fast.get_next() != None and fast.get_next().get_next() != None:
            slow = slow.get_next()
            fast = fast.next.get_next()
        return slow      