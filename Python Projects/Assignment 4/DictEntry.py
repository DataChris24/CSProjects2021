from Map import Map

class DictEntry:
    '''
    Class creates object that stores word and probability.
    Used to place a pair of values in one location in the prefix_to_entry map.
    '''

    def __init__(self, word, prob):
        self.word = word
        self.prob = prob

    def __str__(self):
        return self.word

    def get_word(self):
        '''
        Returns the word associated with object
        '''
        return self.word 

    def get_prob(self):
        '''
        Returns the probability associated with object
        '''
        return self.prob

    def match_pattern(patern):
        # Find out what this is?
        return None
