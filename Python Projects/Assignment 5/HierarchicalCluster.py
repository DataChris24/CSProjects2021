from BinaryTree import BinaryTree

class HierarchicalCluster(BinaryTree):
    def __init__(self, data, name, left_child = None, right_child = None):
        if data == None:
            hc_data = self.compute_centriod(left_child, right_child)
            super().__init__(hc_data, left_child, right_child)
        else:
            super().__init__(data, left_child, right_child)
        if name == None:
            self.name = self.set_name(left_child, right_child)
        else:
            self.name = name
        self.num_children = self.set_children(left_child, right_child)
        
    def compute_centriod(self, left, right):
        '''
        Will compute centroid by computing a weighted average from the
        left and right children's centroids, weighted by the number of
        leaf nodes in each tree.
        '''
        cent_list = []
        for i in range(left.num_children):
            cent_list.append(left.root_data)
        for i in range(right.num_children):
            cent_list.append(right.root_data)
        return_list = []
        sum = 0
        for i in range(len(cent_list[0])):
            for j in range(len(cent_list)):
                row = cent_list[j]
                sum += float(row[i])
            cent_item = sum / len(cent_list)
            return_list.append(cent_item)
            sum = 0
        return return_list

    def set_children(self, left, right):
        '''
        This is a helper method that will set the number of children that
        are leaves.
        Will compute from the number of leaves in each left and right child
        clusters.
        '''
        # If cluster is a leaf node
        if left is None and right is None:
            return 1
        # This should not be hit, but here for completeness
        if left is None and right is not None:
            return right.num_children
        # This should not be hit, but here for completeness
        if right is None and left is not None:
            return left.num_children
        # If cluster has children
        else:    
            return left.num_children + right.num_children

    def set_name(self, left, right):
        '''
        This will set the name as a list of all names of leaf nodes in the
        cluster. 
        '''
        name = []
        for i in range(len(left.name)):
            name.append(left.name[i])
        for j in range(len(right.name)):
            name.append(right.name[j])
        return name
     
    