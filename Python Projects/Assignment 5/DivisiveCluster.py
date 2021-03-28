import csv
from HierarchicalCluster import HierarchicalCluster
from Pair import Pair
from BinaryMinHeap import BinaryMinHeap

clusters = []
root = None

def insert_data(file):
    '''
    This will read in the file and create the initial clusters
    '''
    with open(file, 'r') as file:
        csvfile = csv.reader(file)

        for row in csvfile:
            name = [row[0]]
            data = row[1:]
            temp = HierarchicalCluster(data, name)
            clusters.append(temp)

    file.close()

def create_root():
    name_list = [] 
    data_list = []

    for i in range(len(clusters)):
        name = clusters[i].name
        name_list.append(name)
        data = clusters[i].root_data
        data_list.append(data)

    cent = calc_centroid(data_list)
    root = HierarchicalCluster(cent, name_list)

def get_HC_list(node):
    names = node.name 
    hc_list = []

    for i in range(names):
        temp_name = names[i]
        for i in range(len(clusters)):
            if clusters[i].name == temp_name:
                hc_list.append(clusters[i])
            else:
                continue
    return hc_list

def make_pairs(list):  # Need to put in all possible cominations of pairs including groups
    pairs = []
    for i in range(len(list)):
        clusts = list
        single = []

        single.append(clusts[i])
        del clusts[i]

        clust_data_list = []
        name_list = []
        for j in range(len(clusts)):
            data = clusts[j].root_data
            clust_data_list.append(data)
            name = clusts[j].name
            name_list.append(name)
        centroid1 = calc_centroid(clust_data_list)

        temp1 = HierarchicalCluster(centroid1, name_list)
        temp2 = HierarchicalCluster(single[0].root_data, single[0].name)

        pairs.append(Pair(temp1, temp2))
    return pairs
        
def calc_centroid(list):
        return_list = []
        sum = 0
        for i in range(len(list[0])):
            for j in range(len(list)):
                row = list[j]
                sum += float(row[i])
            cent_item = sum / len(list)
            return_list.append(cent_item)
            sum = 0
        return return_list

def get_min_pair(list):
    heap = BinaryMinHeap()
    heap.build_heap(list)
    return heap.find_min()
    

def build_tree(node):
    if len(node.name) == 1:
        return
    else:
        list = get_HC_list(node)
        pairs = make_pairs(list)
        min_pair = get_min_pair(pairs)
        node.insert


insert_data("simple.csv")
create_root()

