import networkx as nx
import osmnx as ox
import streamlit as st
from locator import lat_lng_from_address

PLACE = "Bangalore, India"

@st.cache_resource
def graph(place: str):
    return ox.graph_from_place(place, network_type="all")

G = graph(PLACE)

source_address = st.text_input("Enter Source Address")
dest_address = st.text_input("Enter Destination Address")

def is_valid_address(lat: float, lng: float) -> bool:
    return lat and lng

if source_address and dest_address:
    from_lat, from_long = lat_lng_from_address(source_address)
    to_lat, to_long = lat_lng_from_address(dest_address)
    print(from_lat, from_long)
    print(to_lat, to_long)

    if is_valid_address(from_lat, from_long) and is_valid_address(to_lat, to_long):
        src_node = ox.nearest_nodes(G, from_lat, from_long) 
        dest_node = ox.nearest_nodes(G, to_lat, to_long) 

        st.write(src_node, dest_node)



#orig_node = ox.nearest_nodes(G, X0, Y0)
#dest_node = ox.nearest_nodes(G, X[0], Y[0])
#
#route = ox.shortest_path(G, orig_node, dest_node, weight="length")
#fig, ax = ox.plot_graph_route(G, route, route_color="y", route_linewidth=6, node_size=0)
#
#st.pyplot(fig)
