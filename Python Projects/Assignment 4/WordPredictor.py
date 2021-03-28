from Map import Map
from DictEntry import DictEntry
import re

class WordPredictor:

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
        prefix_to_entry entries, matching each prefix to the most probable 
        word.
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
                            self.prefix_to_entry.put(s, dict_ent)
                        elif found.prob < prob:
                            self.prefix_to_entry.put(s, dict_ent)
                        else:
                            continue
                    curr_word = curr_word.next
                    curr_count = curr_count.next

    def get_best(self, prefix):
        '''
        Takes in a prefix to a word, prefix, and returns the word associated
        with the best probability, best. If prefix is not in the map, returns
        None.
        '''
        best = self.prefix_to_entry.get(prefix)
        if best == None:
            return None
        else:
            return best

    def get_training_count(self):
        '''
        Returns the total word count
        '''
        return self.total

    def get_word_count(self, word):
        '''
        Takes in a word, word, and returns its assocated count.
        I assume it would return None if the word was not in the map.
        '''
        count = self.word_to_count.get(word)
        if count == None:
            return 0
        else:
            return count

