class Edge:
    def __init__(self, L1, L2, val):
        self.L1 = L1
        self.L2 = L2
        self.val = val

class Graph:
    def __init__(self):
        self.edges = {}
        self.values ={}

    def add_node(self, edge):
        if edge.L1 not in self.edges:
            self.edges[edge.L1] = []
        if edge.L2 not in self.edges:
            self.edges[edge.L2] = []
        self.edges[edge.l1].append((edge.L2, edge.val))
        self.edges[edge.l2].append((edge.L1, edge.val))

