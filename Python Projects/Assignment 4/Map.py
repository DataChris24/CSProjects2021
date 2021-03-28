from HashTable import HashTable
import LinkedList

class Map(HashTable):
    '''
    This class will implement the map of the values for the keys stored in 
    the HashTable. Is the child of HashTable. Most of the code was supplied
    from the notes in week 10. Changes to the put(), get(), hashfunction() 
    and remove() methods.
    '''
    def __init__(self, size=9973):
        '''
        Initializes an object of the Map class. which includes the HastTable
        from the parent.
        '''
        super().__init__(size)
        self.values = [None] * self.size # holds values
        
    def __str__(self):
        '''
        Prints out the map with key:value pair shown
        '''
        s = ""
        for slot, key in enumerate(self.slots):
            value = self.values[slot]
            s += str(key) + ":" + str(value) + ", "
        return s
    
    def __len__(self):
        '''
        Return the number of key-value pairs stored in the map.
        '''
        count = 0
        for item in self.slots:
            if item is not None:
                count += 1
        return count
    
    def __getitem__(self, key):
        '''
        Returns the value stored at the slot and index where the key is found
        '''
        return self.get(key)

    def __setitem__(self, key, data):
        '''
        Adds a key-value pair to the map if key is unique, or updates value
        if key is found.
        '''
        self.put(key,data)
        
    def __delitem__(self, key):
        '''
        Removes the item at the slot and index where the key is found
        '''
        self.remove(key)
        
    def __contains__(self, key):
        '''
        Returns the value stored at the slot and index where the key is found
        '''
        return self.get(key) != -1

            
    def put(self, key, value):
        '''
        Add a new key-value pair to the map. If the key is already in the map 
        then replace the old value with the new value.
        Returns -1 if key was not added to map, therefore value cannot be added
        '''
        slot = super().put(key)
        pos = slot[0]
        if slot == None:
            return None  # when key is not added to the map
        elif self.values[pos] == None:
            # this is when a new key was added and now we need to add a new
            # value to the map
            self.values[pos] = LinkedList.LinkedList()
            self.values[pos].append(value)
        elif slot[2]:
            # this is if the key value was already in the map and we will
            # need to just update the value
            self.values[pos].replace_data(slot[1], value)
        else:
            self.values[pos].append(value)
        
    def get(self, key):
        '''
        Returns the value stored at slot and index of the positon where the
        key is stored in slots, returns -1 if key not found.
        '''
        slot = super().get(key)
        if slot == None: # key doesn't exsist in the map
            return None
        else:
            return self.values[slot[0]].data_index(slot[1])
    
    def remove(self, key):
        '''
        Removes key:value pair.
        Returns slot location if item in hashtable, -1 otherwise
        '''
        slot = super().remove(key)
        if slot == None:
            return None
        else:
            self.values[slot[0]].pop(slot[1])
            return slot[0], slot[1]

    def hashfunction(self, item):
        '''
         Python's standard hash() function
        '''
        key = super().hashfunction(item)
        return key 
