class Graph:
    def __init__(self, num_of_nodes):
        # Initialization of the Graph class with the number of nodes and an empty graph
        self.m_num_of_nodes = num_of_nodes
        self.m_graph = []

    def add_edge(self, node1, node2, weight):
        # Method to add an edge to the graph with specified nodes and weight
        self.m_graph.append([node1, node2, weight])
        
    # Finds the root node of a subtree containing node `i` using the path compression technique
    def find_subtree(self, parent, i):
        if parent[i] == i:
            return i
        # Path compression: set the parent of `i` to the root of the subtree
        parent[i] = self.find_subtree(parent, parent[i])
        return parent[i]

    # Connects subtrees containing nodes `x` and `y` based on their sizes
    def connect_subtrees(self, parent, subtree_sizes, x, y):
        xroot = self.find_subtree(parent, x)
        yroot = self.find_subtree(parent, y)
        # Union by rank: attach the smaller subtree to the root of the larger subtree
        if subtree_sizes[xroot] < subtree_sizes[yroot]:
            parent[xroot] = yroot
        elif subtree_sizes[xroot] > subtree_sizes[yroot]:
            parent[yroot] = xroot
        else:
            # If both subtrees are of the same size, choose one as the root and increment its size
            parent[yroot] = xroot
            subtree_sizes[xroot] += 1
            
    def kruskals_mst(self):
        # List to store the edges of the Minimum Spanning Tree (MST)
        result = []
        
        # Iterator
        i = 0
        # Number of edges in the MST
        edge_count  = 0

        # Sort edges by their weight
        self.m_graph = sorted(self.m_graph, key=lambda item: item[2])
        
        # Auxiliary arrays
        parent = []
        subtree_sizes = []

        # Initialize `parent` and `subtree_sizes` arrays for union-find operations
        for node in range(self.m_num_of_nodes):
            parent.append(node)
            subtree_sizes.append(0)

        # Important property of MSTs:
        # the number of edges in an MST is equal to (m_num_of_nodes - 1)
        # while we haven't yet added each edge
        # increment iterator and run the union find algorithm
        while edge_count  < (self.m_num_of_nodes - 1):
            # Pick an edge with the minimal weight
            node1, node2, weight = self.m_graph[i]
            i = i + 1

            x = self.find_subtree(parent, node1)
            y = self.find_subtree(parent, node2)

            # If nodes don't belong to the same subtree, add the edge to the MST
            if x != y:
                edge_count = edge_count  + 1
                result.append([node1, node2, weight])
                self.connect_subtrees(parent, subtree_sizes, x, y)
        
        # Print the resulting MST and its total weight
        total_weight = 0
        for node1, node2, weight in result:
            print("({}, {}) cost: {}".format(node1, node2, weight))
            total_weight += weight

        print("\nTotal Weight of MST:", total_weight)
            
def main():
    # Example graph with 9 nodes
    example_graph = Graph(9)
    example_graph.add_edge(0, 1, 4)
    example_graph.add_edge(0, 2, 7)
    example_graph.add_edge(1, 2, 11)
    example_graph.add_edge(1, 3, 9)
    example_graph.add_edge(1, 5, 20)
    example_graph.add_edge(2, 5, 1)
    example_graph.add_edge(3, 6, 6)
    example_graph.add_edge(3, 4, 2)
    example_graph.add_edge(4, 6, 10)
    example_graph.add_edge(4, 8, 15)
    example_graph.add_edge(4, 7, 5)
    example_graph.add_edge(4, 5, 1)
    example_graph.add_edge(5, 7, 3)
    example_graph.add_edge(6, 8, 5)
    example_graph.add_edge(7, 8, 12)
    
    # Print the initial graph
    print("\nInitial Graph:")
    for edge in example_graph.m_graph:
        print("({}, {}) cost: {}".format(edge[0], edge[1], edge[2]))
        
    # Find the MST and print the results
    print("\MST:\n")
    example_graph.kruskals_mst()

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()