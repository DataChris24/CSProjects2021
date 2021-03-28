import LinkedList

class HashTable:
    '''
    This class creates a hash table to store keys of the key/value pairs.
    Most code was provided in the lecture materials.
    '''
    def __init__(self, size=9973):
        '''
        Instantiates an object of the class with a hash table with specified
        size, or size = 9973 as default.
        '''
        self.size = size
        self.slots = [None] * self.size
        
    def put(self, item):
        '''
        Place an item in the hash table.
        If collision occurs, check linked list for hashkey,
        if not in liked list, place item's hashkey in linked list
        Return slot number and node number if successful, None
        otherwise (should never happen since we are using a linked list
        for chaining)
        '''
        hashkey = self.hashfunction(item)
        slot_num = hashkey % self.size
        loc = -1
        found = False
        if self.slots[slot_num] == None:
            self.slots[slot_num] = LinkedList.LinkedList()
            self.slots[slot_num].append(item)
            loc = 0
        else:
            if self.slots[slot_num].search(item) == None:
                loc = self.slots[slot_num].append(item)
            else: 
                loc = self.slots[slot_num].search(item)
                found = True
        return slot_num, loc, found

    def get(self, item):
        '''
        returns slot position and node number if item in hashtable, 
        None otherwise
        '''
        hashkey = self.hashfunction(item)
        slot_num = hashkey % self.size
        if self.slots[slot_num] == None:
            return None
        elif self.slots[slot_num] != None and self.slots[slot_num].search(item) == None:
            return None
        else:
            return slot_num, self.slots[slot_num].search(item)

    def remove(self, item):
        '''
        Removes item.
        Returns slot position if item in hashtable, None otherwise
        '''
        hashkey = self.hashfunction(item)
        slot_num = hashkey % self.size  
        
        loc = self.slots[slot_num].remove(item)

        return slot_num, loc

    def hashfunction(self, item):
        '''
        Uses the default hast() function from python, then used modulo for 
        bucket number
        '''
        return hash(item)
