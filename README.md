# Algorithms-for-MST
> This is a project created for the final project of the Network Flow Optimization subject of the Master's Degree in Computer science of the [University of Cagliari](https://www.unica.it/unica/en/homepage.page).

# About 
This repository provides implementations of Minimum Spanning Tree (MST) algorithms, with a focus on two popular approaches: Kruskal and Prim. A Minimum Spanning Tree is a subset of edges from a connected graph that connects all nodes without forming cycles and has the minimum possible total weight.

#Kruskal's Algorithm
Kruskal's Algorithm is a greedy algorithm that constructs an MST by repeatedly selecting the edge with the lowest weight, ensuring that no cycles are formed. The crucial step in Kruskal involves managing disjoint sets to ensure selected edges do not create cycles in the graph.

#Prim's Algorithm
Prim's Algorithm starts with a single node and grows the MST by adding the edge with the lowest weight at each step, ensuring that the newly added node is connected to the existing MST to maintain connectivity.
