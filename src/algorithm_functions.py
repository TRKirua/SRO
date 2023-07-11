import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import shortest_path, connected_components
from scipy.optimize import linear_sum_assignment
from itertools import combinations

def sum_edges(graph):
    return np.sum(graph) / 2

def get_odd_vertices(graph):
    return [index for index, degree in enumerate(np.sum(graph > 0, axis=1)) if degree % 2]

def chinese_postman(graph):
    graph = csr_matrix(graph)
    n_components, labels = connected_components(csgraph=graph, directed=False, return_labels=True)

    if n_components > 1:
        raise ValueError("The graph has more than one connected component.")

    odd_vertices = get_odd_vertices(graph)
    if not odd_vertices:
        return sum_edges(graph.toarray())

    shortest_paths = shortest_path(graph)

    # Map the vertices to new indices
    vertex_to_index = {vertex: index for index, vertex in enumerate(odd_vertices)}

    # Create a matrix for the odd vertices
    odd_vertex_matrix = np.zeros((len(odd_vertices), len(odd_vertices)))

    # Fill in the matrix with the shortest path lengths
    for i, j in combinations(odd_vertices, 2):
        # Use the new indices in the odd_vertex_matrix
        index_i = vertex_to_index[i]
        index_j = vertex_to_index[j]
        odd_vertex_matrix[index_i, index_j] = shortest_paths[i, j]
        odd_vertex_matrix[index_j, index_i] = shortest_paths[j, i]

    # Find the minimum weight perfect matching
    row_indices, col_indices = linear_sum_assignment(odd_vertex_matrix)

    # Calculate the added distance
    added_distance = sum(odd_vertex_matrix[i, j] for i, j in zip(row_indices, col_indices)) / 2
    return sum_edges(graph.toarray()) + added_distance