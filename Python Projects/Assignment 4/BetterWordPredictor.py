from Map import Map
from DictEntry import DictEntry
from LinkedList import LinkedList
import re

class BetterWordPredictor:
    def __init__(self):
        self.word_to_count = Map()
        self.total = 0
        self.prefix_to_entry = Map()

    def train(self, file):
        '''
        Will read in a file line by line then break into each word,
        then will send each word to train_word.
        '''
        with open(file, 'r') as text:
            for line in text:
                for word in line.split():
                    self.train_word(word)
        text.close

    def train_word(self, word):
        '''
        Takes a word as input, word, and strips out any non-alphabet characters
        and punctuation, except for when an apostrophe is included in a 
        conjuction, ensures word is lowercase, then adds it to the 
        word_to_count map. Each occurence of a word increases its count.
        Returns nothing.
        '''
        new_word = re.sub(r'[^\w\']+', '', word)
        if new_word.islower(): # word is already all lowercase
            found = self.word_to_count.get(new_word)
            if found == None:
                self.word_to_count.put(new_word, 1)
                self.total += 1
            else:
                self.word_to_count.put(new_word, found + 1)
                self.total += 1
        else:
            new_word = new_word.lower()
            found = self.word_to_count.get(new_word)
            if found == None:
                self.word_to_count.put(new_word, 1)
                self.total += 1
            else:
                self.word_to_count.put(new_word, found + 1)
                self.total += 1

    def build(self):
        '''
        This will walk through all the words in word_to_count and create the 
        prefix_to_entry entries, creating a list of words with the highest
        probability at the beginning of the list and lowest probability at the
        end of the list.
        Returns nothing.
        '''
        for slot, key in enumerate(self.word_to_count.slots):
            words = self.word_to_count.slots[slot]
            counts = self.word_to_count.values[slot]
            if words == None:
                continue
            else:
                curr_word = words.head 
                curr_count = counts.head
                while curr_word != None:
                    word = curr_word.data
                    count = curr_count.data
                    prob = count / self.total
                    dict_ent = DictEntry(word, prob)
                    chars = [char for char in word]
                    s = ""
                    for i in range(len(chars)):
                        s += chars[i]
                        found = self.prefix_to_entry.get(s)
                        if found == None:
                            list = LinkedList()
                            list.append(dict_ent)
                            self.prefix_to_entry.put(s, list)
                        else:
                            self.prefix_to_entry.values[found[0].data_index(found[1])]

