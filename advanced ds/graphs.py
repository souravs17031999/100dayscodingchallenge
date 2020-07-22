class adjnode:
    def __init__(self, data):
        self.data = data
        self.next = None

class graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adjlist = [None]*self.V

    def add_edge(self, src, dst):
        new_node_dst = adjnode(dst)
        new_node_dst.next = self.adjlist[src]
        self.adjlist[src] = new_node_dst

        new_node_src = adjnode(src)
        new_node_src.next = self.adjlist[dst]
        self.adjlist[dst] = new_node_src

    def print_adjlist(self):
        for i in range(self.V):
            print(f'vertex {i} :', end = " ")
            ptr = self.adjlist[i]
            while(ptr):
                print(f'-> {ptr.data}', end = " ")
                ptr = ptr.next
            print()

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
