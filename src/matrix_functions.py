import numpy as np

# Get list of nodes
def get_nodes(G):
    return list(G.nodes)

# Get list of edges
def get_edges(G):
    return list(G.edges(data=True))

# Create an initial zero matrix
def initialize_matrix(size):
    return np.zeros((size, size))

# Get node indices
def get_node_indices(node_list, node1, node2):
    return list(map(node_list.index, (node1, node2)))

# Update matrix elements
def update_matrix(matrix, indices, value):
    matrix[(*indices, ), (*reversed(indices), )] = value
    return matrix

# Process each edge of the graph
def process_edge(matrix, node_list, edge):
    node1, node2, edge_data = edge
    indices = get_node_indices(node_list, node1, node2)
    return update_matrix(matrix, indices, edge_data['length'])

# Modelization of a street/city network
def from_graph_to_matrix(G):
    node_list = get_nodes(G)
    edge_list = get_edges(G)
    result_matrix = initialize_matrix(len(node_list))

    for edge in edge_list:
        result_matrix = process_edge(result_matrix, node_list, edge)

    return result_matrix, node_list

# Initialize node list
def initialize_node_list(size):
    return [[i] for i in range(size)]

# Associating a node to the matrix
def associate_node_to_matrix(G, l):
    node_list = initialize_node_list(l)

    for index, node_data in zip(range(l), G.nodes):
        node_list[index].append(node_data)

    return node_list