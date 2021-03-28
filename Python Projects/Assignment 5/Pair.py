import math

class Pair:
    def __init__(self, HC_memb1, HC_memb2):
        self.HC_memb1 = HC_memb1
        self.HC_memb2 = HC_memb2
        self.dist = self.compute_distance()

    def __lt__(self, other):
        if self.dist < other.dist:
            return self
        else:
            return other

    def compute_distance(self):
        data1 = self.HC_memb1.root_data
        data2 = self.HC_memb2.root_data

        sum = 0

        for i in range(len(data1)):
            sum += (float(data1[i]) - float(data2[i]))**2
        
        return math.sqrt(sum)

    