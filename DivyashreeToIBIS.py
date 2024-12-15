import networkx as nx
import osmnx as ox

PLACE = "Bangalore, India"

G = ox.graph_from_place(PLACE, network_type="all")

'''
G = ox.routing.add_edge_speeds(G)
G = ox.routing.add_edge_travel_times(G)

gdf_nodes, gdf_edges = ox.graph_to_gdfs(G)

divyasree_coords = (12.94838590023717, 77.69309112318902)
iisc_coords = (13.017108084382844, 77.56712358271811)

orig = ox.distance.nearest_nodes(G, X = divyasree_coords[0], Y = divyasree_coords[1])
dest =  ox.distance.nearest_nodes(G, X = iisc_coords[0], Y = iisc_coords[1])

k_routes = ox.k_shortest_paths(G, orig, dest, 30, weight="length")
'''
points = ox.utils_geo.sample_points(ox.convert.to_undirected(G), n=100)

X = points.x.values
Y = points.y.values
X0 = X.mean()
Y0 = Y.mean()

orig_node = ox.nearest_nodes(G, X0, Y0)
dest_node = ox.nearest_nodes(G, X[0], Y[0])

route = ox.shortest_path(G, orig_node, dest_node, weight="length")
fig, ax = ox.plot_graph_route(G, route, route_color="y", route_linewidth=6, node_size=0)

