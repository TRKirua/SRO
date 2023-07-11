import osmnx as ox
import numpy as np

# Saving map for a better visualization
def save_map(graph, filename):
    map_graph = ox.plot_graph_folium(graph, popup_attribute='name', edge_width=2)
    map_graph.save(filename)

# Choice of the street/city
def graph_from_place(place):
    G = ox.graph_from_place(place, network_type="drive")
    return G