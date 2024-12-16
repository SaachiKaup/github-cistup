import networkx as nx
import osmnx as ox
import streamlit as st

PLACE = "Bangalore, India"

@st.cache_resource
def graph(place: str):
    return ox.graph_from_place(place, network_type="all", simplify = False)

def add_lengths(G):
    return ox.distance.add_edge_lengths(G)  

G = graph(PLACE)
G = add_lengths(G)

src_lat_lng = st.text_input("Enter Source Latitude, Longitude")
dest_lat_lng = st.text_input("Enter Destination Latitude, Longitude")

def is_valid_address(lat: float, lng: float) -> bool:
    return lat and lng

if src_lat_lng and dest_lat_lng: 
    from_lat, from_long = list(map(float, map(lambda x: x.strip(), src_lat_lng.split(","))))
    to_lat, to_long = list(map(float, map(lambda x: x.strip(), dest_lat_lng.split(","))))
    print(from_lat, from_long)
    print(to_lat, to_long)

    if is_valid_address(from_lat, from_long) and is_valid_address(to_lat, to_long):
        src_node, src_dist = ox.nearest_nodes(G, from_lat, from_long, return_dist = True) 
        dest_node, dest_dist = ox.nearest_nodes(G, to_lat, to_long, return_dist = True) 

        print(src_node, src_dist, dest_node, dest_dist)

        routes = ox.k_shortest_paths(G, src_node, dest_node, k = 3, weight = "length")
        fig, ax = ox.plot_graph_routes(G, routes, route_color = "y", route_linewidth = 3)
        st.pyplot(fig)
