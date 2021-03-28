import csv
from HierarchicalCluster import HierarchicalCluster
from Pair import Pair
from BinaryMinHeap import BinaryMinHeap
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

clusters = []
leaves = []


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

def make_pairs():
    '''
    This makes pairs from the list of clusters
    '''
    pairs = []
    for i in range(len(clusters)):
        for j in range(i + 1, len(clusters)):
            temp = Pair(clusters[i], clusters[j])
            pairs.append(temp)
    return pairs

def delete_clust(pair):
    clust1 = pair.HC_memb1
    clust2 = pair.HC_memb2

    for i in range(len(clusters)):
        if clusters[i] == clust1:
            del clusters[i]
            break
        else:
            continue

    for j in range(len(clusters)):
        if clusters[j] == clust2:
            del clusters[j]
            break
        else:
            continue

def build_clusters():
    while len(clusters) > 1:
        pair_list = make_pairs()
        heap = BinaryMinHeap()
        heap.build_heap(pair_list)
        min_pair = heap.find_min()
        delete_clust(min_pair)
        new_clust = HierarchicalCluster(None, 
                                        None, 
                                        min_pair.HC_memb1, 
                                        min_pair.HC_memb2)
        clusters.append(new_clust)
    return clusters[0]

def build_graph(save_name):
    df_list = []
    index = []
    for i in range(len(leaves)):
        data_point = []
        row = leaves[i]
        first = row[0]
        name = first[0]
        index.append(name)
        data_list = row[1]
        for j in range(len(data_list)):
            point = float(data_list[j])
            data_point.append(point)
        df_list.append(data_point)
    df = pd.DataFrame(df_list, index = index)
    plt.pcolor(df)
    if len(index) < 10:
        plt.yticks(np.arange(0.5, len(df.index), 1), df.index)
        plt.savefig(save_name)
    else:
        plt.savefig(save_name) 

def get_leaves(root):
    # if node is None
    if root is None:
        return
    
    # if node has left child, check for leaf recursively
    if root.left_child:
        get_leaves(root.left_child)

        # if node is a leaf
    if root.left_child is None and root.right_child is None:
        leaves.append([root.name, root.root_data])
        return
        
    # if node has right child, check for leaf recursively
    if root.right_child:
        get_leaves(root.right_child)


def main():
    file = input("Please enter a filename of a csv: ")
    save_name = input("Please enter a filename for output: ")
    insert_data(file)
    tree = build_clusters()
    get_leaves(tree)
    build_graph(save_name)
    print("Check your files for your image.")

if __name__=="__main__":
    main()