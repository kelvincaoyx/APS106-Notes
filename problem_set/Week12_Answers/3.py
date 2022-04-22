import random

class Node:
    '''Represent a labeled node with a varying number of outgoing edges'''
    
    def __init__(self, label = ""):
        '''
        (self, str) -> NoneType
        '''
        self.label = label
        self.outgoing_edges = []
    
    def __str__(self):
        '''
        (self) -> str
        '''
        return self.label

    def add_outgoing_edge(self, edge):
        '''
        (self, Edge) -> NoneType
        Add a new outgoing edge
        '''
        self.outgoing_edges.append(edge)
        
    def simpler_find_path(self, end):
        '''
        (self, Node) -> List of str
        Recursively finds a path from self to end. A simpler implementation
        '''
        #print("Trying:", self.label)
              
        if end == self:        # base case
            return [self.label]
        
        returned_list = []
        i = 0
        while (not returned_list) and i < len(self.outgoing_edges):
            returned_list = self.outgoing_edges[i].tail.simpler_find_path(end)
            i += 1
        
        if returned_list:
            return [self.label] + returned_list
        else:
            return []
        

    def find_path(self, end, path_so_far):
        '''
        (self, Node, list of str) -> List of str
        Recursively finds a path from self to end. 
        '''
        path_so_far.append(self.label)
        #print("Trying:", self.label)
              
        if end == self:        # base case
            return path_so_far
        
        returned_list = []
        i = 0
        while (not returned_list) and i < len(self.outgoing_edges):
            returned_list = self.outgoing_edges[i].tail.find_path(end,path_so_far)
            i += 1
        
        if not returned_list:
            print("No path from", self.label)
            path_so_far.pop()
        
        return returned_list
            
        
class Edge:
    '''Represent a weighted, directed edge between two Nodes'''
    
    def __init__(self, weight, head, tail):
        '''
        (self, num, Node, Node) -> NoneType
        Initialize an Edge between head and tail
        '''
        self.weight = weight
        self.head = head
        self.tail = tail

def create_graph(filename):
    ''' 
    (str) -> dictionary of Nodes
    Read in and construct a graph from the file filename.
    '''
    nodes = {}
    with open(filename, "r") as infile:
        for row in infile:
            fields = row.strip().split(" ")
            print(fields)
            
            if fields[0] == "Node": # node line
                # create new Node and add it to the dictionary
                n = Node(fields[1])
                nodes[n.label] = n
            elif fields[0] == "Edge":
                head = nodes[fields[2]]
                tail = nodes[fields[3]]
                e = Edge(int(fields[1]), head, tail)
                head.add_outgoing_edge(e)
            else:
                print("Unrecognized line\n", row, "\nSkipping it")
                
    return nodes


nodes = create_graph("exam\Week12_Answers\graph.txt")
print(nodes)
node_labels = list(nodes.keys())

#path = nodes["A"].simpler_find_path(nodes["C"])
#print("Path from A to C:", path, flush=True)


# pick 5 random nodes and find a path between them
for i in range(5):
    source_label = node_labels[random.randint(0,len(node_labels)-1)] # pick a random source
    target_label = node_labels[random.randint(0,len(node_labels)-1)] # pick a random target
    print("Path from ", source_label, " to ", target_label, ":", sep="",end="", flush=True)
    path = nodes[source_label].simpler_find_path(nodes[target_label])
    print(path)

# some code that you probably want to test with first
#source_label = "A"
#target_label = "E"
#print("Path from", source_label, "to", target_label, ":", end="", flush=True)
#path = << find a path >>>
#print(path)
