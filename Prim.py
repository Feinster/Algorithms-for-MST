import time
import random

class Graph:
    def __init__(self, num_of_nodes):
        self.m_num_of_nodes = num_of_nodes
        # Initialize the adjacency matrix with zeros
        self.m_graph = [[0 for column in range(num_of_nodes)] 
                    for row in range(num_of_nodes)]

    def add_edge(self, node1, node2, weight):
        # Add an edge to the graph with the given weight
        self.m_graph[node1][node2] = weight
        self.m_graph[node2][node1] = weight

    def prims_mst(self, debug=False):
        
        start_time = time.time()  
        
        # Defining a really big number, that'll always be the highest weight in comparisons
        positive_inf = float('inf')

        # This is a list showing which nodes are already selected 
        # so we don't pick the same node twice and we can actually know when to stop looking
        selected_nodes = [False for node in range(self.m_num_of_nodes)]

        # Matrix of the resulting MST
        result = [[0 for column in range(self.m_num_of_nodes)] 
                    for row in range(self.m_num_of_nodes)]

        # Index to keep track of iterations
        indx = 0

        # Print the initial graph for reference
        if debug:
            print("Initial graph (adjacency matrix):\n")
            for i in range(self.m_num_of_nodes):
                print(self.m_graph[i])
            print("\n")

        # While there are nodes that are not included in the MST, keep looking:
        while(False in selected_nodes):
            # We use the big number we created before as the possible minimum weight
            minimum = positive_inf

            # The starting node
            start = 0

            # The ending node
            end = 0

            for i in range(self.m_num_of_nodes):
                # If the node is part of the MST, look at its relationships
                if selected_nodes[i]:
                    for j in range(self.m_num_of_nodes):
                        # If the analyzed node has a path to the ending node AND it's not included in the MST (to avoid cycles)
                        if (not selected_nodes[j] and self.m_graph[i][j] > 0):  
                            # If the weight path analyzed is less than the minimum of the MST
                            if self.m_graph[i][j] < minimum:
                                # Defines the new minimum weight, the starting vertex and the ending vertex
                                minimum = self.m_graph[i][j]
                                start, end = i, j

            # Since we added the ending vertex to the MST, it's already selected:
            selected_nodes[end] = True

            # Filling the MST adjacency matrix fields:
            result[start][end] = minimum

            if minimum == positive_inf:
                result[start][end] = 0

            # Print the edge that is added to the MST
            if debug:
                print("adding edge %d. (%d - %d): cost: %d" % (indx, start, end, result[start][end]))
            indx += 1

            # Make the MST undirected by adding the reverse edge
            result[end][start] = result[start][end]

        # Print the resulting MST and its total weight
        total_weight = 0
        
        # Print the resulting MST
        if debug:
            print("\nMST:\n")
            for i in range(len(result)):
                for j in range(0+i, len(result)):
                    if result[i][j] != 0:
                        print("({}, {}) cost: {}".format(i, j, result[i][j]))
                        total_weight += result[i][j]
        
            print("\nTotal Weight of MST:", total_weight)
        
        end_time = time.time()  
        execution_time = end_time - start_time 
        print("\nExecution time with {} nodes: {}".format(self.m_num_of_nodes, execution_time))

def main():
    # Example graph has 9 nodes
    graph = Graph(9)
    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 2, 7)
    graph.add_edge(1, 2, 11)
    graph.add_edge(1, 3, 9)
    graph.add_edge(1, 5, 20)
    graph.add_edge(2, 5, 1)
    graph.add_edge(3, 6, 6)
    graph.add_edge(3, 4, 2)
    graph.add_edge(4, 6, 10)
    graph.add_edge(4, 8, 15)
    graph.add_edge(4, 7, 5)
    graph.add_edge(4, 5, 1)
    graph.add_edge(5, 7, 3)
    graph.add_edge(6, 8, 5)
    graph.add_edge(7, 8, 12)
    
    # Run Prim's algorithm and print the resulting MST
    graph.prims_mst(debug=True)
    
    comparative_test=False
    
    if comparative_test:
        for num_of_nodes in range(5, 1000, 100):
            graph = Graph(num_of_nodes)

            for i in range(num_of_nodes - 1):
                random_weight = random.randint(1, 10)  
                graph.add_edge(i, i + 1, random_weight)

            graph.prims_mst()

# Run the main function
if __name__ == "__main__":
    main()
