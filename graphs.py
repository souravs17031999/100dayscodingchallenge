# program to implement adjacency list representation of graphs in python
# IDEA: logic is to maintain a list of vertices as a list and then use linked list for storing all adjacent nodes for that particular vertex corresponding to the index of the list and each value in the list will store the address of the first node attached to it (head pointer for linked list).

# class to represent node structure
class adjnode:
    def __init__(self, data):
        self.data = data
        self.next = None

# class to represent graph and its methods
class graph:
    # intializing the graph with vertices as the size of list and then initilse the list with None values
    def __init__(self, vertices):
        self.V = vertices
        self.adjlist = [None]*self.V

    # simply creating the new node and updating the head as we are adding new edge at the start of the list which takes 0(1) time
    def add_edge(self, src, dst):
        new_node_dst = adjnode(dst)
        new_node_dst.next = self.adjlist[src]
        self.adjlist[src] = new_node_dst

        # use this because graph is assumed to be undirected, in case of other , no need to use this.
        new_node_src = adjnode(src)
        new_node_src.next = self.adjlist[dst]
        self.adjlist[dst] = new_node_src

    # going over every list item one by one and traverse over the linked list appened to that item.
    def print_adjlist(self):
        for i in range(self.V):
            print(f'vertex {i} :', end = " ")
            ptr = self.adjlist[i]
            while(ptr):
                print(f'-> {ptr.data}', end = " ")
                ptr = ptr.next
            print()


# another implementation of graph optimized : by using defaultdict from collections and passing list as argument -> defautdict(list) so that each key is a vertex and keys are list of nodes which are appended and newer keys are automatically added into the dictionery as it is the property of that.


# main function 
if __name__ == '__main__':
    g = graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 4)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.print_adjlist()
