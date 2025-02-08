import networkx as nx
import osmnx as ox
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import geopandas as gpd



# turn response caching off
ox.settings.use_cache = True


# explore a neighborhood's buildings + street network interactively
cf = '["highway"~"service|footway|steps"]'
cols = ["wheelchair", "access"]
cols2 = ["name", "addr:unit", "description"]
place = "Gewerbepark Deutsches Brennstoffinstitut, Freiberg, Sachsen, Deutschland"

G = ox.graph.graph_from_place(place, network_type="all", retain_all=True, custom_filter=cf) 
gdf = ox.features.features_from_place(place, tags={"building": True})
gdf2 = ox.features.features_from_place(place, tags={'access': 'delivery', 'ref': 'poststation_dbi_09599'})
m = gdf.explore(tiles="cartodbdarkmatter",tooltip=cols2)
m = gdf2.explore(m=m,tooltip=cols,color= "red")

ox.convert.graph_to_gdfs(G, nodes=False).explore(m=m, color="yellow")


#save as html in Img folder 
#m.save("../Img/Gewerbepark Deutsches Brennstoffinstitut.html")



## Finding the shortest path to all Entrances

# Define origin node
origin = 3989756446

tags = {'access': 'delivery', 'wheelchair': 'yes', 'ref': 'poststation_dbi_09599'}

# Filter nodes to only those with the tag  'access': 'delivery' or 'ref': 'poststation_dbi_09599'
nodes_access = ox.features.features_from_place(place, tags=tags)

nodes = nodes_access[(nodes_access["access"] == "delivery")| (nodes_access["ref"] == "poststation_dbi_09599")]

if nodes.empty:
    raise ValueError("No entrance nodes found in the graph.")

# Convert entrance points to nearest graph nodes
nodes = [
    ox.nearest_nodes(G, x, y) for x, y in zip(nodes.geometry.x, nodes.geometry.y)
]

# Compute shortest paths to all entrance nodes
routes = []
for dest in nodes:
    try:
        route = nx.shortest_path(G, origin, dest, weight="length")
        routes.append(route)
    except nx.NetworkXNoPath:
        print(f"No path found to entrance node {dest}")

if not routes:
    raise ValueError("No valid routes found.")

# Plot the graph
fig, ax = ox.plot_graph(G, show=False, close=False, node_size=0)

# Plot all routes
ox.plot_graph_routes(G, routes, route_colors="y", route_linewidth=2, node_size=0, ax=ax)

plt.show()


#save as png
#fig.savefig("../Img/Routing_to_all_entrances.png")



## Routing to all accesible entrances


sum_distance = 0.0  # in meters

# Filter nodes to only those with the attribute 'entrance'
nodes_access = ox.features.features_from_place(place, tags=tags)
nodes = nodes_access[((nodes_access["access"] == "delivery") & (nodes_access["wheelchair"] == "yes"))| (nodes_access["ref"] == "poststation_dbi_09599")]



# Convert entrance points to nearest graph nodes
r_nodes = [
    ox.nearest_nodes(G, x, y) for x, y in zip(nodes.geometry.x, nodes.geometry.y)
]

# Compute shortest paths to all entrance nodes
routes = []
for dest in r_nodes:
    try:
        route = nx.shortest_path(G, origin, dest, weight="length")
        distance= nx.shortest_path_length(G, origin, dest, weight="length")
        sum_distance += distance
        
        routes.append(route)
    except nx.NetworkXNoPath:
        print(f"No path found to entrance node {dest}")

print(f"Total distance: {sum_distance} meters")

if not routes:
    raise ValueError("No valid routes found.")

# Plot the graph
fig, ax = ox.plot_graph(G, show=False, close=False, node_size=0)

# Plot all routes
ox.plot_graph_routes(G, routes, route_colors="y", route_linewidth=2, node_size=0, ax=ax)

plt.show()

#save as png
fig.savefig("../Img/Routing_to_all_accesible_entrances.png")
